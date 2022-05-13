class Symbol:
    """
    This class contains all the 4 symbols (hearts, diamonds, clubs and spades) and colors
    that can be found in a deck of cards
    """
    
    icon_list = ['♥', '♦', '♣', '♠']
    color_list = ["red", "black"]
 
    def __init__(self, color: str, icon: str):
        """ This method is a class constructor
            It consists of two attributes:
            1. color: which is of type sting
            2. icon: which is a list of string
        """
        self.color = color 
        self.icon = icon
        self.check()

    def check(self):
        if (self.icon in self.icon_list) and (self.color in self.color_list):
            if (self.color == "red") and (self.icon != '♥') and (self.icon != '♦'):
                    print("Only heart and diamond can be red")
            if (self.color == "black") and (self.icon != '♣' and self.icon != '♠'):
                    print("Only Club and Spade can be black")     
        else:
            print("Your icon or color is invalid") 

    def __str__(self):
       return f"The card is {self.color} {self.icon}"

class Card(Symbol):
    """
    This class contains all the numeric values from 2-10 and
    alphabets A, J, Q and K that can be found in a deck of cards
    """
    
    value_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 

    def __init__(self, color, icon, value: str):
        super().__init__(color, icon)
        self.value = value
        self.check_value()

    def check_value(self):
        if self.value not in self.value_list:
            print("Your value is invalid")    
    
    def __str__(self):
       card_value = super().__str__()    
       return f"{card_value}  of value {self.value}"

