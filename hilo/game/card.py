import random

class Card:
    """
    Cretes the card class
    """

    def __init__(self):
        """
        Creates the card with a starting value of 0
        """

        self.value = 0

    def draw_card(self):
        """
        Adjusts the card value by drawing a random card
        """

        #Adjusts value to random number 1-13
        self.value = random.randint(1, 13)

