import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_message(self, message_txt):
        account_sid = os.environ.get('ENV_TWILIO_SID')
        auth_token = os.environ.get('ENV_TWILIO_TOKEN')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=os.environ.get('ENV_TWILIO_FROM'),
            body=message_txt,
            to=os.environ.get('ENV_TWILIO_TO')
        )
