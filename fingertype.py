"""
On July 1st the program called fingertips was shut down, which was a program that allowed you to type shortcuts to write longer texts.
This is a simple program that mimics the functionality of fingertips. But made in Python.
"""

import keyboard
import time
from shortcuts import Shortcuts


class Main:
    def __init__(self):
        self.keys = []
        self.shortcut_map = Shortcuts().shortcut_map

    def on_key_press(self, event):
        if event.event_type == keyboard.KEY_UP:
            return

        # Pressing these keys will clear the key list
        if event.name in ["enter", "tab"]:
            self.keys = []
            return

        modifier_keys = [
            "ctrl",
            "shift",
            "alt",
            "esc",
            "up",
            "down",
            "left",
            "right",
            "caps lock",
            "alt gr",
            "left windows",
            "delete",
        ]

        # Dont log the key if it is a modifier key
        if event.name in modifier_keys:
            return

        # check if any of the above keys are pressed when another key is pressed, example: ctrl + c. if a shortcut is pressed, do not add the modifier key to the list
        if any(keyboard.is_pressed(mod) for mod in modifier_keys):
            return

        if event.name == "space":
            #  The "shortcut" is all the keys pressed before the space
            shortcut = "".join(self.keys)
            # Check if the shortcut is in the shortcut map
            if shortcut in self.shortcut_map:
                # Get the long text from the shortcut map
                long_text = self.shortcut_map[shortcut]
                # If the long text is a function, call it, so we can dynamically add a timestamp or similar
                if callable(long_text):
                    long_text = long_text()

                # Clear the shortcut itself and the space
                for _ in range(len(shortcut) + 1):  # +1 to remove the space as well
                    keyboard.press_and_release("backspace")

                # Short delay to ensure backspaces are processed before typing the long text
                time.sleep(0.1)

                # Type the long text
                keyboard.write(long_text + " ")
                print(f"Shortcut detected: {shortcut} -> {long_text}")

            # Reset keys buffer after processing space
            self.keys = []

        # If the key is backspace, remove the last key from the list
        elif event.name == "backspace":
            try:
                self.keys.pop()
            except IndexError:  # If the list is empty
                pass
        # Add the key to the list
        else:
            self.keys.append(event.name)

        print(self.keys)

    def run(self):
        # Start the keyboard listener
        keyboard.hook(self.on_key_press)
        keyboard.wait()


if __name__ == "__main__":
    app = Main()
    app.run()
