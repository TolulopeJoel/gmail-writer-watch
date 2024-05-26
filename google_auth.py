import json
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def save_credentials(creds):
    with open('token.json', 'w') as token_file:
        token_file.write(creds.to_json())

def load_credentials():
    if os.path.exists('token.json'):
        with open('token.json', 'r') as token_file:
            creds = Credentials.from_authorized_user_info(json.load(token_file), SCOPES)
            return creds
    return None

def get_auth_service():
    creds = load_credentials()
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=7001)
            save_credentials(creds)
    
    service = build('gmail', 'v1', credentials=creds)
    return service

if __name__ == '__main__':
    service = get_auth_service()
