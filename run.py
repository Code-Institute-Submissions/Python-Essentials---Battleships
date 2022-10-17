# Global variable for the grid
game_grid = [[]]
# Global variable for the grid size
grid_size = 0
# Global variable for the grid level
grid_level = 0
# Global variable for the untargeted grid coordiantes
ocean_wave = "~"


# the function below will set the game grid size
def setGridLevel(): 
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


# the function below shall compose and print a grid set to the size input by the user
def make_grid(ocean_wave, grid_level):
    # set rows as empty strings
    header_row = ''
    standard_row = ''
    # compose the rows and seperating characters, loop as many times as stated in grid_level +1 to ensure 5 playable rows are printed
    for num in range(1,grid_level+1):
        # creates the header numbers
        header_row = header_row + '|' + str(num)
        # creates the playing area
        standard_row = standard_row + '|' + ocean_wave 
    print(header_row + '|')
    print('-' * (len(standard_row)+1))
    # Apply alphabetical characters to the rows for coordiantion
    char = 64
    for x in range(1,grid_level+1):
        char = char  +1 
        print(chr(char) + standard_row + '|')
    print(f" BOMBS AHOY!\n")


# main function
def main():
    setGridLevel()
    make_grid(ocean_wave, grid_level)

main()