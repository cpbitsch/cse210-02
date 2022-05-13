from game.card import Card

class Director:
    """
    Creates the Director class that is used to control the game
    """
    def __init__(self):
        """
        Initializes the object and sets the attributes
        """
        self.is_playing = True
        self.points = 300
        self.card = Card()
    
    def get_card(card):
        """
        Calls the draw_card function from the Card class to generate a random card
        """

        #calls function 
        Card.draw_card(card)
        #sets the value = to the value on the card
        card_value = card.value

        return card_value

    def card_vs_input(self, current_card, new_card, player_input):
        """
        Function that checks if the current card is greater or less than the new card drawn.
        Then checks that value against the user input to determine if chose correct or not.
        """

        #if current card is greater than new card and user guessed lower
        if current_card > new_card and player_input == "l":
            win = True
        #if current card is greater than new card and user guessed higher
        elif current_card > new_card and player_input == "h":
            win = False
        #if current card is less than new card and user guessed higher
        elif current_card < new_card and player_input == "h":
            win = True
        #if current card is less than new card and user guessed lower
        elif current_card < new_card and player_input == "l":
            win = False
        #If current card is equal to new card
        elif current_card == new_card:
            win = "tie"
        
        return win
            
    def adjust_points(self, win, points):
        """
        Function that calculates points. Uses the card_vs_input function to set the value of win
        """

        #if player guess correctly
        if win == True:
            points += 100
        #if player guess incorrectly
        elif win == False:
            points -= 75
        #if the results were the same
        elif win == "tie":
            points = points

        return points

    def game_loop(self):
        """
        Runs the game
        """

        #Gets the value of the first card
        current_card = self.get_card()

        #main game loop
        while self.is_playing:
            
            #sets the value of the next card
            new_card = self.get_card()

            print()
            #prints current card
            print(f"The card is: {current_card}")
            #gets player guess whether card is higher or lower
            player_input = input("Higher or lower? [h/l]: ")

            #if player inputs anything other than "h" or "l" loops through until they do
            while player_input != "h" and player_input != "l":
                player_input = input("Higher or lower? [h/l]: ")

            #prints new card
            print(f"Next card was: {new_card}")
            
            #calls function to check if user guessed correctly
            win = self.card_vs_input(current_card, new_card, player_input)
            #calls function to adjust points
            self.points = self.adjust_points(win, self.points)
            #prints points
            print(f"Your score is {self.points}")
            
            #if the adjusted point value is less than or equal to 0 sets is_playing to false
            #and ends the game loop
            if self.points <= 0:
                print("Game Over")
                self.is_playing = False
                break

            #changes the card drawn this turn to the current card
            current_card = new_card
            
            #asks user if wants to play again
            play_again = input("Play again? [y/n]: ")
            
            #if player inputs anything other than "y" or "n" loops through until they do
            while play_again.lower() != "y" and play_again.lower() != "n":
                play_again = input("Play again? [y/n]: ")

            #sets is_playing to true or false depending on user input.
            #y will loop through another round, n will end the program
            #if play_again.lower() == "y":
            #    self.is_playing = True
            #elif play_again.lower() == "n":
            #    print("Thanks for playing")
            #    self.is_playing = False
            if play_again.lower() == "y":
                self.is_playing = True
            elif play_again.lower() == "n":
                print("Thanks for playing")
                input('Did you enjoy playing the game?')
                print('Thank you for your feedback.')
                self.is_playing = False
