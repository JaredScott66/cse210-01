import random

class Dealer():
    """A random Card value generator. Generates a value from 1 to 13.

    Attributes:
        value

    
    """

    def __init__(self):
        """Creates New instance of Dealer.

        Args: self (Dealer) New insrtance of dealer.
        
        """
        self.value = 1
       

    def draw(self):
        """Draws random integer between 1 and 13
        
        """
        self.value = random.randint(1, 13)