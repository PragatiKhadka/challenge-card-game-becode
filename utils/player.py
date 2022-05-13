import random 
from card import Card

class Player:
    """
    This is a class that describes the players. It has following attributes:
    1. card which is a list of Card
    2. turn_count to count the number of times a player has played
    3. number_of_cards to count how many card does a player have
    4. history to record all the cards that (all) players have

    It contains a method play
    """

    history = []

    def __init__(self, name):
        """ Constuctor of the class """
        self.name = name
        self.cards = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0

    def play(self):
        self.turn_count += 1
        my_card = self.cards[random.randint(0, len(self.cards) - 1)]
        self.number_of_cards += 1
        self.history.append(my_card)
        #print(f"{self.name} {self.turn_count} played: {card_num} {card_symbol}")
        
        return my_card

    def __str__(self):
        return f"I am {self.name}"    


class Deck():
    """
    This is a class which contains all the cards with following attributes:
    1. cards which contain a list of instances of Card.
    It will have following methods:
    1. fill_deck(): It will fill cards with a complete card game. It should contain all 52 cards
    2. shuffle(): It will shuffle all the list of cards.
    3. distribute(): It will take a list of Player as parameter and will distribute the cards evenly between all the players.
    """        

    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        """
        This function will fill the deck with 52 cards
        """
        count = 0
        for icon in ['♥', '♦']:
            color = 'red'
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(color, icon, value))
                count += 1
        for icon in [ '♣', '♠']:
            color = 'black'
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(color, icon, value))  
                count += 1
        print(f"{count} cards are added.")        

    def shuffle(self):
        """
        This function shuffles the deck of cards
        """
        self.cards = random.sample(self.cards, len(self.cards))

    def distribute(self, players):
        """
        This method will distribute the cards among the players
        """
        
        rounds = round(len(self.cards) / len(players))
        for i in range(0, rounds):
            print("round: ", i)
            for player in players: 
                if len(self.cards) != 0:
                    card_popped = self.cards.pop()
                    player.cards.append(card_popped)
    
    def __str__(self):
        return (f"{self.cards}") 

new_deck = Deck()
new_deck.shuffle()

names = ['Stefan', 'Pragati','Yuri']
players = []
for i in range(0, len(names)):
    players.append(Player(names[i]))

new_deck.distribute(players)    










