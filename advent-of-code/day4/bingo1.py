

def main():
    # Get ordered list of numbers for bingo
    numberStream = get_number_stream("input.txt")

    # Get list of bingo game boards
    gameGrids = get_bingo_grids("input.txt")

    print()

    

def get_number_stream(file: str) -> list[int]:
    """ Reads the list of ordered bingo numbers on
    the first line of the input file
    """
    result = []
    file_handle = open(file, 'r')

    line = file_handle.readline().strip()
    str_arr = line.split(',')

    for str in str_arr:
        result.append(int(str))
    
    file_handle.close()

    return result

def get_bingo_grids(file: str):
    """ Returns a list of bingo game grids in the
    form a 3d array
    """
    grids = []
    #Open file and read past the first line 
    file_handle = open(file, 'r')
    file_handle.readline()

    line = file_handle.readline()

    while line.strip() != "end":
        #Get a single bingo grid and add it to the 
        #list of grid
        grid = get_bingo_grid(file_handle)
        grids.append(grid)
        line = file_handle.readline().strip()

    return grids  
    
def get_bingo_grid(file_handle):
    """ Reads and returns a single bingo grid 
    in the shape of a 2d array
    """
    grid = []

    line = file_handle.readline().strip()
    while line != "\n" and line != "end":
        line_arr = line.split(" ")
        # Remove any list items that are empty strings
        for item in line_arr:
            if item == "":
                line_arr.remove(item)

        # Read string values into a tuple with an int 
        # and a boolean to signify if the number is 
        # marked on the game grid
        grid_line = []
        for i in range(len(line_arr)):
            grid_line.append((int(line_arr[i]), False))

        grid.append(grid_line)
        line = file_handle.readline()
        line = line.strip()
    
    return grid


if __name__ == '__main__':
    main()