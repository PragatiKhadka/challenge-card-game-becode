from utils.game import Board

if __name__ == "__main__":
    """
    This is the main program that is used to run the game.
    First of all, it will create a Board class object then ask for the user to provide input
    for number of players and their names. 
    After that it will start the game between the players.
    """
    b = Board()
    b.num_players()     
    b.start_game()   
    print(b)