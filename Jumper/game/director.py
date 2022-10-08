from game.secret_word import Secret_word
from game.jumper import Jumper
from game.revealer import Revealer  

class Director():
    """Directs game operation.
    
    Attributes:
        is_playing:bool
        Secret_word()
        Jumper()
        Revealer()
    """

    def __init__(self):
        """Creates instance of director.

        Args:
            self (Director) an instance of Director.
        """
        self._secret_word = Secret_word()
        self._jumper = Jumper()
        self._revealer = Revealer()
        self.guess = ""
        self._word = ""
        self._word_temp = []
        self._is_playing = True
        self._temp_blank = []

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    
    def _get_inputs(self):
        """Takes player guess and secret word to compare.

        Args:
            self (Director): an instance of Director.
        """
        self._word = self._secret_word.new_word()
        self.guess = input("What letter?: ")
        


    def _do_updates(self):
        """Updates jumper and word templates to reflect progress made in game

        Args:
            self (Director): an instance of Director.
        """
        word_list = self._revealer.list_word(self._word)
        #self._revealer.do_compare(word_list, self.guess)
        self._word_temp = self._revealer.list_word(word_list)

        
            

    def _do_outputs(self):
        """Displays jumper as lines are cut, and the word as its revealed.

        Args:
            self (Director): an instance of Director.
        """

        print(self._word_temp)
        print(self._word)
        stop = input("stop?")
        if stop == "y":
            self._is_playing = False