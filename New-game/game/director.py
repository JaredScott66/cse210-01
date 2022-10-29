from game.text_get import GetText
from game.Scene import Scene

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
        self._branch = 0
        self._item = ""
        self._choice = ""
        self._get_text = GetText()
        self._path = ""


    def start_game(self):
        """Starts game and runs the game loop.

        Args:
            self(Director) An instance of director.
        """
        print("Welcome to the text based adventure game.\nGHOST SHIP\nLets begin!\n")
        print("You wake on an abandoned space craft. Everything is silent...\nYou see a distant blinking light in a darkened room to the left.\nThere is a door directly in front that says Engine Room.\nTo the right there is a cabinet with a loose lock.\nYou walk over to the cabinet. It reads on the door. Sr Mechanic John Tayler\nWith the lock being open you easily open it.\nInside you can see some clothes and assorted tools. Among them you find: A keycard, a pistol with a single bullet, and an engine manual. What do you take?")
        self._item = input("KEY\nGUN\nENGINE\n")
        self._get_text.file_read("New-game\game\Text\step_1.txt")
        self._text = self._get_text.get_text()
        self._get_text.set_choice("New-game\game\Text\choice_1.txt")
        self._choice = self._get_text.get_choice()
        while self._is_playing == True:
            self._get_inputs()
            self._do_updates()
            #self._do_outputs()

    def _get_inputs(self):
        """Gets input from player according to the choice made from the given scenario.

        Args:
            self(Director) An instance of Director
        """
        print("test")
        self._player_input = input(f"{self._text}\n{self._choice}\n")

    def _do_updates(self):
        """Updates game state and variables.

        Args:
            self(Director) An instance of Director.
        """
        set_scene = Scene()
        set_scene.set_scene(self._branch, self._player_input)
        self._path = set_scene.get_scene()
        
        self._branch += 1
        file_scene = (f"New-game\game\Text\step_{self._path}.txt")
        file_choice = (f"New-game\game\Text\choice_{self._path}.txt")

        get_text = GetText()
        get_text.file_read(file_scene)
        self._text = get_text.get_text()

        get_choice = GetText()
        get_choice.file_read(file_choice)
        self._choice = get_text.get_text()

    #def _do_outputs(self):
        #print(self._text)
        #print(self._choice)