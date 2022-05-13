### challenge-card-game-becode

The game consists of two (complete)files: ```card.py``` and ```player.py```.  Other two files ```main.py``` and ```game.py``` is not done.

### card.py  
This file consists of two class ```Symbol``` and ```Card```. The ```Card``` class is inherited from the ```Symbol``` class.  
To instantiate a Card object, three parameteres are required:  
1. color  
2. icon  
3. value  
Example: card = Card("red", '♦', '10')



### player.py  
This file also contains 2 classes ```Player``` and ```Deck```. 
```Deck``` class consists of the deck of cards with functions to shuffle the card and distribute the cards among the players.  
For testing purpose, a list of 3 players are made among which the cards will be distributed. 




