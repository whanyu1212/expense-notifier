import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError


class GmailService:

    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    CLIENT_SECRET_FILE = "/Users/hanyuwu/Study/expense_notify/client_secret_465835940757-qvh7pe9berbhkeh2v9ubaqfo2k9bh2ug.apps.googleusercontent.com.json"

    def __init__(self):
        self.service = self.authenticate_gmail()

    def authenticate_gmail(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            self.CLIENT_SECRET_FILE, self.SCOPES
        )
        creds = flow.run_local_server(port=0)
        service = build("gmail", "v1", credentials=creds)
        return service

    def send_email(self, to, subject, body):
        message = MIMEText(body)
        message["to"] = to
        message["subject"] = subject
        encoded_message = {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            sent_message = (
                self.service.users()
                .messages()
                .send(userId="me", body=encoded_message)
                .execute()
            )
            print(f'Sent message to {to} Message Id: {sent_message["id"]}')
        except HTTPError as error:
            print(f"An error occurred: {error}")
            sent_message = None
        return sent_message


# Usage
if __name__ == "__main__":
    gmail_service = GmailService()
    gmail_service.send_email(
        "whanyu47@gmail.com", "test email", "This is the body of the email"
    )
