# Global variable for the grid
game_grid = [[]]
# Global variable for the grid size
grid_size = 0
# Global variable for the grid level
grid_level = 0
# Global variable for the untargeted grid coordiantes
ocean_wave = " ~ "


def setGridLevel(): 
    """
    This function shall fire first and shall welcome the user to the game
    and request that they input a number between 5 and 20. This figure is used
    to set how difficult the game shall be by altering the size of the playable grid.
    The code will validate the user input by checking if the figure is an integer, equal to 
    or less then 5 and equal too or less than 20.
    """
    global grid_level
    
    while True:
        try:
            # parse the user input as an integer assign this to the grid_level variable.
            grid_level = int(input(f"Enter a whole number between 5 and 20 to set the difficulty.\nThe number input shall set the size of the games grid.\n"))
            # check if input is between 5 and 20 if yes continue otherwise print error. 

            if grid_level >= 5 and grid_level <= 20:
                print(f"Setting difficulty...\n")

            else:
                print(f"Your input is not within the range, please input an number between 5 and 20.\n")
                continue

        # print valueError is input is not a an integer and restart loop
        except ValueError:
            print(f"Your input is not valid, please input an integer, e.g. a whole number between 5 and 20.\n")
            continue

        else:
            # if input is valid, print chosen level and return false to close the while loop
            print(f"You selected Level {grid_level}. Game Ready.\n")
            return False


def make_grid(ocean_wave, grid_level):
    """
    This function will build a sequence of lists which shall then be used,
    later in this script to print the playing area of the game to the terminal.
    """
    global game_grid
    # set rows and columns to the returned grid_level int.
    rows, columns = (grid_level, grid_level)

    # Create an empty list for the playing area
    game_grid = []

    # loop through the number of rows 
    for row in range(rows):
        row = []
        # for every column append a wave 
        for col in range(columns):
            row.append(ocean_wave)
        # append the return lists to the game_grid variable
        game_grid.append(row)


def print_play_area():
    global game_grid

    # create a string of the alphabet to be used as coordiantes
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # pull the relevant amount of characters from above into a new variable and print the Header.
    game_size = characters[0: len(game_grid) + 1]
    print("  BOMBS AHOY!  ")
    
    # for each row within game grid, print the corresponding letter.
    for row in range(len(game_grid)):
        print(characters[row], end="| ")
        # then for every column in game_grid print the symbol representing a wave
        for col in range(len(game_grid[row])):
            # this code will check for the placement of a ship 
            if game_grid[row][col] == "O":
                print(ocean_wave, end=" ")
            else:
                print(game_grid[row][col], end=" ")
        print("")


# main function
def main():
    setGridLevel()
    make_grid(ocean_wave, grid_level)
    print_play_area()

main()