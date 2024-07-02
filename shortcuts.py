"""
This module is where the shortcuts are defined.
"""

import datetime


class Shortcuts:
    """
    This class contains the shortcuts that can be used in the program.
    """

    def __init__(self):
        """
        Initialize the shortcuts.
        """
        self.shortcut_map = {
            "mvg": "Met vriendelijke groeten,\n\nMax Koets",
            "mailc": "Opdracht ligt compleet in het magazijn\n\nMet vriendelijke groeten,\n\nMax Koets",
            "sig": self.get_signature_text,
        }

    def get_current_timestamp(self):
        """
        Get the current timestamp in the format "dd-mm-yyyy hh:mm".
        """
        return datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    def get_signature_text(self):
        """
        Get the signature text with the current timestamp.
        """
        return f"{self.get_current_timestamp()} MKO:"
