# Writer Watcher

## Project Description

Writer Watcher is a tool I created to solve the inconvenience of manually tracking when my favorite writers post new articles. It extracts blog links from your Gmail email (draft), monitors these blogs using RSS feeds, and sends you email notifications whenever new content is published.

<img width="461" alt="Screenshot 2024-05-30 at 2 30 32 AM" src="https://github.com/TolulopeJoel/gmail-writer-watcher/assets/95661346/b2bb9a38-331d-464a-ba28-b0cab83e929a">

## Features

- **Feed Monitoring**: Tracks feeds for new articles from your favorite writers.
- **Email Notifications**: Sends an email notification with details of the new articles.
- **Automatic Blog Management**: Fetches new blogs from Gmail and updates the list of monitored blogs.

## Requirements

- Python 3+
- Gmail account with OAuth 2.0 credentials
- RSS feed links of your favorite writers
- Gmail email ID
- Gmail email containing new blog links.
example:
<img width="460" alt="Screenshot 2024-05-30 at 1 49 37 AM" src="https://github.com/TolulopeJoel/gmail-writer-watcher/assets/95661346/ac34b6a1-58e6-47c3-94cc-28ba466caa42">

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TolulopeJoel/writer-watcher.git
   cd writer-watcher
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory of the project.
   - Add the following environment variables:
     ```
     EMAIL_DRAFT_ID=your_email_id_containg_links
     EMAIL_TO=your_email@example.com
     EMAIL_FROM=seeus@seahorse.com
     ```

5. **Add Gmail API credentials**:
   - Obtain OAuth 2.0 client credentials from the [Google Cloud Console](https://console.cloud.google.com/).
   - Save the `credentials.json` file in the root directory of the project.

6. **Create an initial `blogs.json` file**:
   ```json
   []
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Access the application**:
   Open your web browser and go to `http://localhost:5000/new`. The application will check for new articles and send an email if any are found.


## License

This project is licensed under the MIT License.


## Nice to Haves

- [x] Sort posts by published date
- [ ] Seperate 'new' writers posts from main email body. When you add a new blog link to your draft,<br />
the application can't tell which posts from that blog you've read, so it sends all posts from the<br />
newly added blog. Seperate these so you can easily distinguish newly added blog links from<br />
updates on blogs you already read.


## Author

- [Tolu Joel](https://tolulopejoel.github.io/)
