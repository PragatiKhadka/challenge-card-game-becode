### challenge-card-game-becode

The game consists of following files:
1. card.py  
2. player.py  
3. game.py
4. main.py 

### card.py  
This file consists of two class ```Symbol``` and ```Card```. The ```Card``` class is inherited from the ```Symbol``` class.  
To instantiate a Card object, three parameteres are required:  
1. color  
2. icon  
3. value  
Example: card = Card("red", '♦', '10')


### player.py  
This file contains 2 classes ```Player``` and ```Deck```. 
```Deck``` class consists of the deck of cards with functions to shuffle the card and distribute the cards among the players.  

### game.py 
This file contains a class ```Board```. This is the class which contains the method to start the game  

### How to play the game  
1. Download the repo.  
2. run the `main.py` file using `python main.py` command  
3. It will ask to enter number of players and their names. Please provide it.  
4. The game will be started and at each round you will be able to see which player played which card on which round. At the end of the game, turn count and number of card





