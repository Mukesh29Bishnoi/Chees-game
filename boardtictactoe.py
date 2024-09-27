
from move import Move
from player import Player

class Board:
    
    EMPTY_CELL = 0
    
    def __init__(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
        
    def print_board(self):
        print("\nPostions")
        self.print_board_with_positons()
        
        print("Board:")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("  |", end="")
                else:
                    print(f"{column} |", end="")
            print()
        print()
        
    def print_board_with_positons(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]
        
        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
            
        else:
            print("This postiton alredy taken . Pleae enter another one!")
   
    def check_is_game_over(self, player, last_move):
        return ((self.check_row(player, last_move))
                or (self.check_column(player, last_move))
                or self.check_diagonal(player)
                   or (self.check_antidiagonal(player)))
    
    def check_row(sefl, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]