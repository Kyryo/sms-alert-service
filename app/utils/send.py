import requests


class Send:

    def __init__(self, url, params, headers) -> None:
        self.url = url
        self.params = params
        self.headers = headers

    def message(self):
        """sends SMS to recipients through the twilio API 

        Returns:
            bool: True if message is sent successfully
        """
        #!   [TODO] handle the exception better - handle specific exception and not just everything, that's bad code!

        try:

            r = requests.post(self.url, json=self.params, headers=self.headers)

        except Exception as e:
            #! [TODO] replace print with logging
            print("DevOps, some error occured:", e)
            return False

        else:

            r.raise_for_status()

            #! [TODO] replace print with logging
            print('sent successfully', r.json())

            return True
