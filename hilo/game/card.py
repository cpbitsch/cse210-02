import random

class Card:
    """
    Cretes the card class
    """

    def __init__(self):
        """
        Creates the card with a starting value of 0 and an empty suit
        """

        self.value = 0
        self.suit = ''

    def draw_card(self):
        """
        Adjusts the card value by drawing a random card
        """

        #Adjusts value to random number 1-13
        self.value = random.randint(1, 13)

    def draw_card_suit(self):
        """
        Adjusts the card suit by drawing a random suit
        """

        a = random.randint(1,4)

        if a == 1:
            self.suit = 'Hearts'
        
        if a == 2:
            self.suit = 'Diamonds'

        if a == 3:
            self.suit = 'Clubs'
        
        if a == 4:
            self.suit = 'Spades'

