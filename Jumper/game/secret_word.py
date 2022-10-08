import random


class Secret_word():
    """The word that the player is trying to guess.
    This class is in charge of choosing a random word to be guessed.

    Attributes:
        word (string) 
    """

    def __init__(self):
        """Creates new instance of Secret_word.

        Args:
            self (Secret_word) New instance of Secret_word
        """
        self._word = ""
        self.word_temp = []


    def new_word(self):
        """Generates new word.
        
        Args:
            self (Secret_word) New instance of Secret_word
        """
        word_list = ["steel", "cheese", "pumpkin", "train", "apple", "panda"]
        index_choice = random.randint(0, 5)
        self._word = word_list[index_choice]

        return self._word
    