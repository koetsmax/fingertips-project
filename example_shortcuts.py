"""
This module is where the shortcuts are defined. Rename this to shortcuts.py
"""

import datetime
import keyboard


class Shortcuts:
    """
    This class contains the shortcuts that can be used in the program.
    """

    def __init__(self):
        """
        Initialize the shortcuts.
        """
        self.shortcut_map = {
            "sc1": "With kind regards,\n\nYour name",
            "sig": self.get_signature_text,
            "sc3": self.get_sc3_text,
        }

    def get_current_timestamp(self) -> str:
        """
        Get the current timestamp in the format "dd-mm-yy hh:mm".
        """
        return datetime.datetime.now().strftime("%d-%m-%y %H:%M")

    def get_signature_text(self) -> str:
        """
        Get the signature text with the current timestamp.
        """
        return f"{self.get_current_timestamp()} initials:"

    def get_sc3_text(self) -> None:
        # Type the subject of the message
        keyboard.write("email subject")

        # Simulate pressing the Tab key to move to the next input field
        keyboard.press_and_release("tab")

        # Type the rest of the message
        keyboard.write(
            "text,\n\n" "text\n\n" "text\n\n\n" "With kind regards,\n\n" "your name"
        )

        # Return an empty string since the message has already been handled
        return ""
