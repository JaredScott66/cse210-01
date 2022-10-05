

class Revealer():
    """Responsible for revealing letters as they are guessed correctly, or cutting lines as they are guessed wrong
    
        Attributes:
            revealed_word (string)
    """

    def __init__(self):
        """Creates new instance of Revealer

            Args:
                self (Revealer) an instace of Revealer.
        """
        self._revealed_word = []
        self._word = []
        self.word_temp = []

    def do_compare(self, word, guess):
        """Takes word and compares it against player guess

            Args:
                self (Revealer) Instance of Revealer
                word (list) The word getting guessed
                guess (string) The player input letter
        """
        for i in word:
            if i == guess:
                self.word_temp.append(guess)
                

    def list_word(self, word):
        """Makes a word into a list.

            Args: 
                self (Revealer) and instance of Revealer
                word (string) word to be made a list.
        """
        w_list = list(word)
        return w_list

    def template(self):
        for i in :
            self.word_temp.append