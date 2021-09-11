import phonenumbers
import logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)


class Validate:

    def __init__(self, data) -> None:
        self.data = data

    def has_required_keys(self) -> bool:
        """validates data coming in to ensure it has all required keys

        Args:
            data (dictionary): contains payload - read documentation for contents

        Returns:
            bool: True if specified key is available
        """

        expected_keys = ("message", "recipient")

        if not all(keys in self.data for keys in expected_keys):

            return False

        return True

    def is_valid_phone_number(self) -> bool:
        """checks if phone number submitted is valid

        Args:
            data ([dict]): contains payload - read documentation for contents

        Returns:
            bool: True if phone number is valid
        """
        #! [TODO] maybe could help to specify the exceptions to handle, however, right now all we want to know is if the phone number provided is a valid phone number, so that works for now.
        try:
            phone_number = phonenumbers.parse(self.data['recipient'], None)

        except Exception as e:
            #! [TODO] change print to logging
            print("DevOps, some error occured:", e)

        else:

            if not phonenumbers.is_valid_number(phone_number):
                return False

        return True
