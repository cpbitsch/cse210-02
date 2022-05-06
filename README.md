# cse210-02

    Classes:
	  Director: Manages the game and game objects
		  Methods:
			  Start game
			  Game loop
			  Get player input
			  Call card object
			  Evaluate card versus player input
			  Keep track of points
			  End the game
		  Attributes:
			  Bool game state (has the game ended yet?)
			  Points
			  (If we make a deck instead of random numbers) Deck

	  Card: Generates a number between 1 and 13, stores that value
		  Methods:
			  Generate a number between 1 and 13
		  Attributes:
			  Card value

	  (We may not make an actual deck object, only if we have time)
	  Deck: Create and store the cards of a deck
		  Methods:
			  Pull a card, remove it from the deck
		  Attributes:
			  List of all cards in the deck (52)
