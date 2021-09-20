import os
from typing import Any
from twilio.rest import Client


class Send:

    def __init__(self, params: dict[str, str]) -> None:
        self.params = params

    def message(self):
        """sends SMS to recipients through the twilio API 

        Returns:
            bool: True if message is sent successfully
        """
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        #!   [TODO] handle the exception better - handle specific exception and not just everything, that's bad code!
        try:
            message = client.messages \
                .create(
                    body=self.params["body"],
                    from_=self.params["sender"],
                    to=self.params["recipient"]
                )

        except Exception as e:
            #! [TODO] replace print with logging
            print("admin, some error occured:", e)
            return False

        else:

            #! [TODO] replace print with logging
            print('sent successfully', message.sid)

            return True
