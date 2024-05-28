from datetime import datetime

import dateutil.parser
import feedparser


def fetch_recent_articles(blog: dict) -> list:
    """
    Fetch recently posted articles for a specific blog.
    """
    blog_link = blog.get('blog')
    feed_link = f'{blog_link}feed/?type=rss'

    if feed_dates := get_latest_feed_entry_date(feed_link):
        latest_date, formatted_date = feed_dates
        last_modified_date = dateutil.parser.parse(blog['lastModified'] or '1999')

        if latest_date > last_modified_date:
            articles = gather_feed_articles(feed_link, last_modified_date)
            if articles:
                blog['lastModified'] = formatted_date
            return articles
    return []


def gather_feed_articles(feed_link: str, last_modified_date: datetime) -> list:
    """
    Gather articles from the RSS feed since the last modified date.
    """
    new_articles = []
    feed = feedparser.parse(feed_link)

    for entry in feed.entries:
        entry_date, formatted_entry_date = parse_feed_date(entry.published_parsed)
        if entry_date > last_modified_date:
            article = {
                'title': entry.title,
                'link': entry.link,
                'published': formatted_entry_date,
            }
            new_articles.append(article)

    return new_articles


def get_latest_feed_entry_date(feed_url: str) -> tuple:
    """
    Get the latest entry date from the RSS feed.
    """
    rss_feed = feedparser.parse(feed_url)
    if rss_feed.entries:
        latest_entry = rss_feed.entries[0]
        entry_date = latest_entry.get('published_parsed')

        return parse_feed_date(entry_date)


def parse_feed_date(date_list: list) -> tuple:
    """
    Convert parsed date to datetime object and formatted string.
    """
    year, month, day, hour, minute = date_list[:5]
    parsed_date = datetime(year, month, day, hour, minute)
    formatted_date = parsed_date.strftime('%a, %d %b %Y %H:%M')

    return parsed_date, formatted_date
