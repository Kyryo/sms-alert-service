import phonenumbers


class Validate:

    def __init__(self, data) -> None:
        self.data = data

    def has_required_keys(self) -> bool:
        """validates data coming in to ensure it has all required keys

        Args:
            data (dictionary): data from request

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

        phone_number = phonenumbers.parse(self.data['recipient'], None)

        if not phonenumbers.is_valid_number(phone_number):
            return False

        return True
