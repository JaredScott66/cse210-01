

class Director():
    """Directs flow of game.

    Attributes:
        text(string) String to be outputted the player.
        player_input(String) String supplied from player
    """
    def __init__(self):
        """Creates new instance of director.

        Args:
            text(string) String to be outputted the player.
            player_input(String) String supplied from player.
            is_playing(bool) Determins if game continues.
        """
        self._text = ""
        self._player_input = ""
        self._is_playing = True


    def start_game(self):
        """Starts game and runs the game loop.

        Args:
            self(Director) An instance of director.
        """
        print("Welcome to the text bases adventure game.\nGHOST SHIP\nLets begin!\n")
        while self._is_playing == True:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def get_inputs(self):
        """Gets input from player according to the choice made from the given scenario.

        Args:
            self(Director) An instance of Director
        """
        self._player_input = input("")
