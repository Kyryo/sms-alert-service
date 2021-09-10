import phonenumbers


class Validate:

    def check_keys(data) -> bool:
        """validates data coming in to ensure it has all required keys

        Args:
            data (dictionary): data from request

        Returns:
            bool: False specified key is not available
        """

        expected_keys = ("message", "recipient")

        if not all(keys in data for keys in expected_keys):

            return False

        return True

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
