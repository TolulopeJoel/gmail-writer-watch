# Gmail Writer Watcher

## Project Description

Gmail Writer Watcher is a Flask-based web application that monitors your favorite writers' blogs and sends you an email notification whenever they publish new articles. It uses RSS feeds to track new posts and Gmail API to send email alerts.

## Features

- **RSS Feed Monitoring**: Tracks RSS feeds for new articles from your favorite writers.
- **Email Notifications**: Sends an email notification with details of the new articles.
- **Automatic Blog Management**: Fetches new blogs from an email draft and updates the list of monitored blogs.

## Requirements

- Python 3+
- Gmail account with OAuth 2.0 credentials
- RSS feed links of your favorite writers
- Gmail draft email containing new blog links
- Gmail draft ID

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TolulopeJoel/gmail-writer-watcher.git
   cd gmail-writer-watcher
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
     EMAIL_DRAFT_ID=your_email_draft_id
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

## Author

- [Tolu Joel](https://tolulopejoel.github.io/)
