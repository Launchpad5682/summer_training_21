from __future__ import print_function
from email import message
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
# MIME Text
from email.mime.text import MIMEText
from email.header import Header
import base64

# If modifying these scopes, delete the file token.json.
# credentials.json must be present in the same directory

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.send']


# creating message
def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """

    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    # converting the MIMEText to string and then into bytes
    message = message.as_string()
    message = bytes(message, 'utf-8')
    # sending the base64.urlsafe_b64encode data in decoded format to the message.send()
    return {'raw': base64.urlsafe_b64encode(message).decode()}


"""
This was creating error while execution
def send_message(service, user_id, message):
    Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    

    message = service.users().messages().send(
        userId=user_id, body=message).execute()

    print('Message Id: %s' % message['id'])
    return message


    except errors.HttpError, error:
        print 'An error occurred: %s' % error
    
"""


def main(message_text):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

        # email
        to = "launchpad5682@gmail.com"
        sender = "saurabh22suthar@gmail.com"
        subject = "This is a system generated mail"
        #message_text = "Hello, this is the message text"

        message = create_message(sender=sender, to=to,
                                 subject=subject, message_text=message_text)

        message = service.users().messages().send(
            userId="me", body=message).execute()
        print(message)
        return None


"""
if __name__ == '__main__':
    main()
"""

# future scope add the exception handling to the code
