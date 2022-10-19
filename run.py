import random
import snoop

# # Global variable for the grid
# game_grid = [[]]
# # Global variable for the grid copy to track ships 
# hit_tracker = [[]]
# # Global variable for the grid size
# grid_size = 0
# # Global variable for the grid level
# grid_level = 0


def setGridLevel(): 
    """
    This function shall fire first and shall welcome the user to the game
    and request that they input a number between 3 and 10. This figure is used
    to set how difficult the game shall be by altering the size of the playable grid.
    The code will validate the user input by checking if the figure is an integer, equal to 
    or less then 3 and equal too or less than 10.
    """
    grid_level = 0
    
    while True:
        try:
            # parse the user input as an integer assign this to the grid_level variable.
            grid_level = int(input(f"Enter a whole number between 3 and 10 to set the difficulty.\nThe number input shall set the size of the games grid.\n"))
            # check if input is between 3 and 10 if yes continue otherwise print error. 

            if grid_level >= 3 and grid_level <= 10:
                print(f"Setting difficulty...\n")
                make_grid(grid_level)

            else:
                print(f"Your input is not within the range, please input an number between 3 and 10.\n")
                continue

        # print valueError is input is not a an integer and restart loop
        except ValueError:
            print(f"Your input is not valid, please input an integer, e.g. a whole number between 3 and 10.\n")
            continue

        else:
            # if input is valid, print chosen level and return false to close the while loop
            print(f"You selected Level {grid_level}. Game Ready.\n")
            return False


def make_grid(grid_level):
    """
    This function will build a sequence of lists which shall then be used,
    later in this script to print the playing area of the game to the terminal.
    """
    game_grid = [[]]
    hit_tracker = [[]]
    # set rows and columns to the returned grid_level int.
    rows, columns = (grid_level, grid_level)

    # loop through the number of rows 
    for row in range(rows):
        row = []
        # for every column append a wave 
        for col in range(columns):
            row.append("~")
        # append the return lists to the game_grid variable
        game_grid.append(row)
        hit_tracker.append(row)
    build_ships(grid_level, game_grid, hit_tracker)
    print_play_area(game_grid)


def build_ships(grid_level, game_grid, hit_tracker):

    ships_to_place = 0
    enemy_counter = 0

    if grid_level < 4:
        ships_to_place = 2
    elif grid_level > 4 and grid_level < 8:
        ships_to_place = 5
    elif grid_level > 8:
        ships_to_place = 7

    while enemy_counter != ships_to_place:
        heading = random.choice(["north", "south", "east", "west"])
        latitude = random.randint(0, grid_level - 1)
        longitude = random.randint(0, grid_level - 1)
        if grid_level < 4:
            ship_size = random.randint(1, 2)
        elif grid_level > 4 and grid_level < 8:
            ship_size = random.randint(1, 4)
        elif grid_level > 8:
            ship_size = random.randint(1, 5)
        if place_ship(latitude, longitude, heading, ship_size, grid_level, game_grid, hit_tracker):
            enemy_counter += 1


def place_ship(latitude, longitude, heading, size, grid_level, game_grid, hit_tracker):
    # the variables below define where to begin 
    # and end the placement of the ships
    lat_start = latitude
    lat_end = latitude + 1
    long_start = longitude
    long_end = longitude + 1 
    # if the randomly generated heading is north
    if heading == "north":
        # check is the length generated for the ship is less than 0  
        if latitude - size < 0:
            # returns false to prevent placement off grid
            return False
        # if true will set the starting latitude of the ship to the 
        # length of the latitude row, minus the size of the ship but plus 1 
        lat_start = latitude - size + 1

    elif heading == "east":
        if longitude + size >= grid_level:
            return False
        long_end = longitude + size
    
    elif heading == "south":
        if latitude + size >= grid_level:
            return False
        lat_end = latitude + size

    if heading == "west":
        if longitude - size < 0:
            return False
        long_start = longitude - size + 1


    return validate_grid_and_place_ship(lat_start, lat_end, long_start, long_end, game_grid, hit_tracker)


def print_play_area(game_grid):
    debug_mode = True
    # create a string of the alphabet to be used as coordiantes
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("   BOMBS AHOY!")
    # for each row within game grid, print the corresponding letter.
    for row in range(len(game_grid)):
        print(characters[row], end="| ")
        # then for every column in game_grid print the symbol representing a wave
        for col in range(len(game_grid[row])):
            # this code will check for the placement of a ship 
            if game_grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print("~", end=" ")
            else:
                print(game_grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for num in range(len(game_grid)):
        print(str(num), end=" ")
    print("")


def main():
    setGridLevel()
    # make_grid()
    # # build_ships()
    # print_play_area()
    

main()