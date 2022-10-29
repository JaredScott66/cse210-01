import csv

from fileinput import close


class GetText:
    """Arranges text to player input. Reads text data to apply to the game

    Attributes:
        file(string) text file for the game scenarios
        text(string) the text to be applied the gane
        choices(list) List of items to be presented to the player.
    """
    def __init__(self):
        """Constructs an instant of GetText.

        Args:
            self(GetText) an instance of GetText.
        """
        self._file = ""
        self._text = ""
        self._choices = ""

    def file_read(self, file):
        
        with open(file, "r") as text_file:

            self._text = text_file.read()

        text_file.close()
    
    def get_text(self):
        return self._text

    def set_choice(self, file):

        with open(file, "r") as choice_file:

            self._choices = choice_file.read()

        choice_file.close()

    def get_choice(self):
        return self._choices