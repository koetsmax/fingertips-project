"""
This module is where the shortcuts are defined.
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
            "mvg": "Met vriendelijke groeten,\n\nMax Koets",
            "mailc": "Opdracht ligt compleet in het magazijn\n\nMet vriendelijke groeten,\n\nMax Koets",
            "sig": self.get_signature_text,
            "magc": self.get_mag_text,
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
        return f"{self.get_current_timestamp()} MKO:"

    def get_mag_text(self) -> None:
        # Type the first part of the message
        keyboard.write("Complete orders en alles wat op naam van de klant staat")

        # Simulate pressing the Tab key to move to the next input field
        keyboard.press_and_release("tab")

        # Type the rest of the message
        keyboard.write(
            "Hi Collega,\n\n"
            "Hierbij een overzicht voor wat er voor 'jouw' klanten klaar staat.\n\n"
            "Complete orders:\n\n\n"
            "Complete order en incompleet: (dit lijkt overbodig maar geeft wel inzicht of er al deel van de bestelling klaar staat)\n\n\n"
            "Met vriendelijke groeten,\n\n"
            "Max Koets"
        )

        # Return an empty string since the message has already been handled
        return ""
