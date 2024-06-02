import base64


def fetch_email_draft(service, draft_id):
    """Fetch and return the body of a draft email by its ID."""
    draft = service.users().drafts().get(userId='me', id=draft_id).execute()
    message = draft.get('message')
    payload = message.get('payload')
    return extract_plain_text_body(payload)


def extract_plain_text_body(payload):
    """Extract and decode the text/plain body from the payload."""
    message_parts = payload.get('parts')

    if message_parts:
        for part in message_parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                return base64.urlsafe_b64decode(data).decode('utf-8')
    else:
        data = payload['body']['data']
        return base64.urlsafe_b64decode(data).decode('utf-8')
