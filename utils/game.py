from utils.player import Deck, Player
import time

class Board:
    """ 
    This class consists variables for storing values such as players, turn_count, active_cards and history_cards.
    It also has method to start the game and num_of_players
    """
    def __init__(self):
        """ Constuctor of the class """
        self.players = []
        self.turn_count: int = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        """
        start the game by making the deck, shuffling it and distributing it to the players 
        until the final round
        """
        my_deck = Deck()
        my_deck.shuffle()
        my_deck.distribute(self.players)  
        
        rounds = round(52 / len(self.players))
        for i in range(0, rounds):
            print("------------------New Round--------------------------\n")
            time.sleep(5)
            self.active_cards = []
            self.turn_count += 1
            for player in self.players:                
                active_card = player.play()
                self.active_cards.append(active_card)
                if i != rounds -  1:
                    self.history_cards.append(active_card)    
                  
            for i in range(0,len(self.players)):
                print("active cards: ", self.active_cards[i].__str__())
    
    def num_players(self):
        """
        This function takes user input where user has to enter the number of players and their names
        """
        num_of_players = int(input("Please enter number of players: "))
        for i in range(0, num_of_players):
            name = input(f"Please enter name of {i+1} player: ")
            self.players.append(Player(name))

    def __str__(self):
        return f"\nturn count: {self.turn_count} \nNo of history cards: {len(self.history_cards)} "



  
