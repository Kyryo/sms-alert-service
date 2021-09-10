import phonenumbers
import requests


class Validate:

    def check_keys(data) -> bool:
        """validates data coming in to ensure it has all required keys

        Args:
            data (dictionary): data from request

        Returns:
            bool: False specified key is not available
        """

        expected_keys = ("api_key", "message", "recipient")

        if not all(keys in data for keys in expected_keys):

            return False

        return True

    def validate_api_key(data) -> bool:
        """ 
        *   validates api_key coming in to check if its authorized to make calls
        *   @param data
        *   return bool
        """

        #! [TODO] connect to a key validation endpoint
        api_key = "6ec4fbee-3dc3-4fa1-9b75-e44d3d78fe06"

        for key in data:
            if data["api_key"] == api_key:
                return True

        return False

    def is_valid_phone_number(data) -> bool:
        """ 
        *   checks if phone number submitted is valid
        *   @param data, dictionary
        *   returns bool
        """

        try:
            phone_number = phonenumbers.parse(data['recipient'], None)
        except:
            return False

        if not phonenumbers.is_valid_number(phone_number):
            return False

        return True


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
