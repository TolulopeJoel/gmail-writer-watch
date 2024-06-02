import asyncio
from datetime import date, datetime

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


@app.route('/')
def home_page():
    day = int(str(date.today()).split('-')[-1])

    now = datetime.now()
    day_of_year = now.timetuple().tm_yday
    # Check if the current year is a leap year
    year = now.year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        total_days_in_year = 366
    else:
        total_days_in_year = 365

    percent_of_year_passed = (day_of_year / total_days_in_year) * 100

    return f"""
    on a journey to become cracked + building what my heart desires
    number of days spent this month: {"❤️ " * day}
    spent {percent_of_year_passed}% of {datetime.now().year}
    """


if __name__ == '__main__':
    app.run()
