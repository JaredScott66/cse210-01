from game.dealer import Dealer

class Director:
    """The user who initalizes the game 

        Attributes: 
            is_playing (bool)
            points (int)
            current_score (int)
            points_added (int)
            points_deducted (int)
    """

    def __init__(self):
        """Starts new instance

        Args:
            Self (Director) instance of director. 
        """

        self.first_card = 0
        self.is_playing = True
        self.current_score = 300
        self.points_added = 100
        self.points_deducted = 75

        f_card = Dealer()
        self.first_card = f_card

    def start_game(self):
        """Starts the game by looping primary game methods.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """Asks user if the card is higher or lower.
        Asks user if they wish to continue play.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your card is: {self.first_card}")
        guess_card = input("Higher or lower? [h/l]")
        

    def do_updates(self):
        """Updates player score
        
        Args:
            Self (Director) instance of director
        """
        if not self.is_playing:
            return
        
        second_card = Dealer()

        if guess_card == "h":
            if self.first_card > second_card:
                self.current_score += self.points_added

            elif self.first_card < second_card:
                self.current_score -= self.points_deducted

        elif guess_card == "l":
            if self.first_card < second_card:
                self.current_score += self.points_added
            
            elif self.first_card > second_card:
                self.current_score -= self.points_deducted

    def do_outputs(self):
        """Displays Card, current points, and asks player if they wish to play again.
        
        Args:
            self (Director): An instance of Director.
        """

        if not self.is_playing:
            return
        
        print(f"Next card was: {second_card}")
        print(f"Your score is: {self.current_score}")
        play_again = input("Play again? [y/n]")
        
        if play_again == "y":
            self.is_playing = True
        else: self.is_playing = False