import re
from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        return bool(re.fullmatch(pattern, number))

    @staticmethod
    def check_name(name):
        pattern = r'[A-Z]+ [A-Z]+'
        return bool(re.fullmatch(pattern, name))