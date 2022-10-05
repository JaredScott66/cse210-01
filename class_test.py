
class Multiply():
    """Multiplies a number.

        Attributes:
           product (num) 
    """
    def __init__(self):
        """Constructs an instance of Multiply.

            Args:
                self (Multiply) an instance of Multiply.
        """
        self._product = 0
    
    def get_product(self):
        """Retreves result of Multiply.
        """
        return self._product
        
    def do_math(self, base, multiplier):
        """Does multipication.
        """
        self._product = (base * multiplier)

class Exponant(Multiply):
    """Calulates an exponant
        Attributs:

    """
    def __init__(self):
        super().__init__()
        self._thing = 0
    
    def make_expo(self, base, expon):
        self._thing = (base ** expon)
    
    def get_expo(self):
        return self._thing

