
class Move:
    
    def __init__(self, value):
        self._value = value
        
    @property
    def value(self):
        return self._value
    
    def is_valid(self)    :
        return 1 <= self._value <= 9
    
    
    def get_row(self):
        if self._value in (1,2,3):
            return 0
        elif self._value in (4, 5, 6):
            return 1
        else:
            return 2
        
    def get_column(self):
        if self._value in (1, 4, 7):  # firsr column
            return 0
        elif self._value in (2, 5, 8):  # second coumn
            return 1
        else:
            return 2
        
