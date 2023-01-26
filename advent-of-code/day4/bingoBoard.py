
class BingoBoard:
    """ This class creates instances of a square board of bingo a game
    """

    def __init__(self, grid):
        self.grid = grid
        self.marked = 0

    def update_number(self, num: int) -> bool:
        """ Checks if number is in grid and if it is 
        updates the boolean value of that tuple to true
        """
        updated = False

        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j][0] == num:
                    self.grid[i][j][1] = True
                    updated = True
                    self.marked += 1
               
        return updated
        
    def _check_rows(self) -> bool:
        for row in self.grid:
            count = 0
            index = 0
            while index < len(row):
                if row[index][1] == True:
                    count += 1
                index += 1
            
            if count == len(self.grid):
                return True
        return False
            
    def _check_columns(self) -> bool:
        for col_index in range(len(self.grid)):
            count = 0
            row_index = 0
            while (row_index < len(self.grid)):
                if self.grid[row_index][col_index][1] == True:
                    count += 1

                row_index += 1

                if count == len(self.grid):
                    return True
        return False
        
    def check_win(self) -> bool:
        """ Checks if there is a column or row with 
        all 5 numbers marked
        """
        return self.__check_rows() or self._check_columns()

    def __repr__(self):
        for row in self.grid():
            for entry in row:
                print(entry[0], end=" ")
                print("\n")
