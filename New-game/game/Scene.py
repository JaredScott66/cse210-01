
class Scene():
    """Controls player scenario.

    Attributes:
        step(int) The current step in the players progress

    """

    def __init__(self):
        """Constructs an instance of Scene

        Args:
            self(Scene) An instance of Scene.
        """
        self._branch = ""
        self._choice = ""
        self._path = ""

    def set_scene(self, branch, choice):
        if branch >= 0 and choice == None:
            self._path = branch
        elif branch >= 0 and choice == str:
            self._path = (f"{branch}_{choice}")
    
    def get_scene(self):
        return self._path