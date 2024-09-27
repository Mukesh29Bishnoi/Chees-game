
import random
class Die:
    
    def __init__(self,):
        self._value = None
        
    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value


class Player:
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10
    
    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        
        return self._counter
    
    def increment_counter(self):
        self._counter += 1
        
    def decrement_counter(self):
        self._counter -= 1
    
    def roll_die(self):
        return self._die.roll()
    
    

class Dicegame:
    
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
       
        
        
    def play(self):
        
        while True:
            
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break
        
    def play_round(self):
        
        print("\n------New Round------")
        input("Press any key to roll the dice.")
        
        #roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()
        
        # Show the value
        self.show_dice(player_value, computer_value)
        
        
        # Determine winner and loser
        if player_value > computer_value:
            print("You won the round!")
            self.update_counter(winner=self._player, losser=self._computer)
            
        elif computer_value > player_value:
            print("The computer won this round . Try again.")    
            self.update_counter(winner=self._computer, losser=self._player)
            
            
        
        else:
            print("It's a tie!")
        
        # Show counter
        self.show_counter()
        
    def print_round_welcome(self):
        print("=============================")
        print("Dice Welcome to Roll a Dice!")
        print("=============================")
        
    def show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}")
        
    def update_counter(self, winner, losser):
        winner.decrement_counter()
        losser.increment_counter()
    
    def show_counter(self)   :
        
        print(f"Your counter:{self._player.counter}")
        print(f"Computer counter:{self._computer.counter}")
        
    def check_game_over(self)  :
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
            
            
        elif self._computer.counter ==0:
            self.show_game_over(self._computer)
            return True
            
    
        else:
            return False
    
    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n================")
            print("G A M E  O V E R ")
            print("The computer won the game.")
            print("==============================")
        
        else:
            print("\n================")
            print("G A M E  O V E R ")
            print("You won the game!.")
            print("==============================")
            

computer_die = Die()
player_die = Die() 
           
my_player = Player(player_die, is_computer= False)      
computer_player =Player(computer_die, is_computer=True)   
   
game = Dicegame(my_player, computer_player)
 
# start the game
game.print_round_welcome()
game.play()
