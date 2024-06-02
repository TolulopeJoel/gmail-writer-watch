import asyncio

from dotenv import load_dotenv
from flask import Flask, jsonify

from blog import add_new_blogs, update_blog_data

load_dotenv()

app = Flask(__name__)


@app.route('/new', methods=['GET'])
def get_new_aricles():
    json_file_path = 'blogs.json'
    add_new_blogs(json_file_path)
    articles = asyncio.run(update_blog_data(json_file_path))
    return jsonify(articles)


if __name__ == '__main__':
    app.run()
