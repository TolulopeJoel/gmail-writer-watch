import asyncio
import base64
import json
import os
from datetime import datetime
from email.message import EmailMessage

import aiohttp
from dotenv import load_dotenv

from draft import fetch_email_draft
from feed import fetch_recent_articles
from google_auth import get_auth_service

# load environment variables
load_dotenv()

EMAIL_DRAFT_ID = os.getenv("EMAIL_DRAFT_ID")

service = get_auth_service()


def get_current_blogs(json_file: str) -> list:
    """
    Return the list of current blogs from JSON file.
    """
    with open(json_file, 'r') as file:
        return json.loads(file.read())


def add_new_blogs(json_file: str):
    """
    Fetch new blogs from email draft and update the blog file.
    """
    blogs = fetch_email_draft(service, EMAIL_DRAFT_ID)
    blogs_list = blogs.split()

    with open(json_file, 'r+') as file:
        data = json.load(file)
        existing_blogs = {entry["blog"] for entry in data}

        for blog_link in blogs_list:
            if blog_link not in existing_blogs:
                dot_index = blog_link.find(".")
                new_blog_entry = {
                    "author": f"{blog_link[8:dot_index]}",
                    "blog": blog_link,
                    "lastModified": "",
                    "type": "RSS"
                }
                data.append(new_blog_entry)

        file.seek(0)
        json.dump(data, file, indent=4)


async def update_blog_data(json_file):
    """Update the blog data with recent articles, send an email if there are new articles."""
    all_new_articles = []
    blogs = get_current_blogs(json_file)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_recent_articles(session, blog) for blog in blogs]
        results = await asyncio.gather(*tasks)

    for new_articles in results:
        all_new_articles.extend(new_articles)

    all_new_articles.sort(
        reverse=True,
        key=lambda x: datetime.strptime(x['published'], "%a, %d %b %Y %H:%M")
    )

    if all_new_articles:
        send_articles(all_new_articles)
        write_blog_data_to_file(json_file, blogs)

    return all_new_articles


def write_blog_data_to_file(json_file: str, blogs: list):
    """
    Write the updated list of blogs back to the JSON file.
    """
    with open(json_file, 'w') as file:
        json.dump(blogs, file, indent=4)


def send_articles(articles: list) -> bool:
    """
    Send an email with the list of new articles.
    """
    message = EmailMessage()
    message_body = "Your faves wrote something!\n\n"
    for article in articles:
        message_body += f"Title: {article['title']}\n"
        message_body += f"Link: {article['link']}\n"
        message_body += f"Published: {article['published']}\n\n ---- \n\n"
    message_body += "with ❤️, Tolu"
    message.set_content(message_body)

    message["To"] = os.getenv("EMAIL_TO")
    message["From"] = os.getenv("EMAIL_FROM")
    message["Subject"] = "new post alert!"

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Send the email
    service.users().messages().send(
        userId="me",
        body={"raw": encoded_message}
    ).execute()


if __name__ == "__main__":
    json_file_path = 'blogs.json'
    add_new_blogs(json_file_path)
    articles = asyncio.run(update_blog_data(json_file_path))
    print(articles)
