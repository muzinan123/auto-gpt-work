import webbrowser
import urllib.parse
import re


def _is_valid_email(email: str) -> bool:
    receivers = email.split(';')
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    for receiver in receivers:
        if not bool(re.match(pattern, receiver.strip())):
            return False
    return True


def send_email(
        to: str,
        subject: str,
        body: str,
        cc: str = None,
        bcc: str = None,
) -> str:
    """Send an email to the specified email address"""

    if not _is_valid_email(to):
        return f"The email address {to} is not valid"
    
    subject_code = urllib.parse.quote(subject)
    body_code = urllib.parse.quote(body)

    mailto_url = f'mailto:{to}?subject={subject_code}&body={body_code}'
    if cc is not None:
        cc = urllib.parse.quote(cc)
        mailto_url += f'&cc={cc}'
    if bcc is not None:
        bcc = urllib.parse.quote(bcc)
        mailto_url += f'&bcc={bcc}'

    webbrowser.open(mailto_url)

    return f"Status: Success\nNote: Email sent to {to}, Subject: {subject}"
