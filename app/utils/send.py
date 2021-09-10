import requests


class Send:

    def __init__(self, url, params, headers) -> None:
        self.url = url
        self.params = params
        self.headers = headers

    def message(self):
        """ 
        *   sends SMS to recipients through the twilio API
        *   @param data, dictionary
        *   returns bool 
        !   [TODO] handle the exception when we fail to send SMS better
        !   [TODO] send data to billing API
        !   [TODO] send data to analytics API 
        """

        try:

            r = requests.post(self.url, json=self.params, headers=self.headers)

        except Exception as e:
            print("DevOps, some error occured:", e)
            return False

        else:

            r.raise_for_status()

            #! [TODO] change this to logging
            print('sent successfully', r.json())

            return True
