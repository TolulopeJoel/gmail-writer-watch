import base64


def fetch_email_draft(service, draft_id: str) -> str:
    """
    Fetches and returns the body of a draft email by its ID.
    """
    draft = service.users().drafts().get(userId='me', id=draft_id).execute()
    message = draft.get('message')
    payload = message.get('payload')

    return extract_plain_text_body(payload)


def extract_plain_text_body(payload: dict) -> str:
    """
    Extracts and decodes the text/plain body from the payload.
    """
    try:
        parts = payload['parts']
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                return base64.urlsafe_b64decode(data).decode('utf-8')
    except KeyError:
        data = payload['body']['data']
        return base64.urlsafe_b64decode(data).decode('utf-8')
