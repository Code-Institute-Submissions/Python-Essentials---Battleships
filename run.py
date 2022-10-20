import random
import snoop
import time

grid_level = 0
game_grid = []
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def setGridLevel(): 
    """
    This function shall fire first and shall welcome the user to the game
    and request that they input a number between 3 and 10. This figure is used
    to set how difficult the game shall be by altering the size of the playable grid.
    The code will validate the user input by checking if the figure is an integer, equal to 
    or less then 3 and equal too or less than 10.
    """
    global grid_level
    
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
    

def fire_cannons():
    global game_grid

    game_running = True
    while game_running: 
        valid_target = False
        while not valid_target:
            target = input(f"To make your shot, enter a Latitude: {characters[0]}-{characters[grid_level-1]}. Then a Longitude from: 0-{grid_level-1} such as 'A1': ")
            target = target.upper()
            if len(target) <= 0 or len(target) > 2:
                print("Misfire! Please enter only one alphabetical character followed by a number e.g. 'A1'")
                continue
            lat = target[0]
            long = target[1]
            if not lat.isalpha() or not long.isnumeric():
                print("Misfire! For the Latitude, please enter a letter. For the Longtitude please enter a Number e.g. 'A1'")
                continue
            lat = characters.find(lat)
            if not (-1 < lat < grid_level):
                print("Misfire! That letter is not on the grid! Please enter a valid letter.")
                continue
            long = int(long)
            if not (-1 < long < grid_level):
                print("Misfire! The number you entered is not on the grid! Please enter a valid number.")
                continue
            if game_grid[lat][long] in ["#", "X"]:
                print("You've hit this location already Captain! Fire again!")
                continue
            if game_grid[lat][long] in ["~", "O"]:
                valid_target = True

        if game_grid[lat][long] == "~":
            print("Captain! Our shot missed! Fire another round!")
            game_grid[lat][long] = "#"
        elif game_grid[lat][long] == "O":
            print("That's a direct hit! Well done Captian!", end=" ")
            game_grid[lat][long] = "X"
        print_play_area(game_grid, grid_level)


def make_grid(grid_level):
    """
    This function will build a sequence of lists which shall then be used,
    later in this script to print the playing area of the game to the terminal.
    """
    global game_grid
    # set rows and columns to the returned grid_level int.
    rows, columns = (grid_level, grid_level)
    # setup empty lists to hold the printed game area and as a method to track shots later
    # game_grid = []
    hit_tracker = []
    # loop through the number of rows
    for _ in range(rows):
        row = ["~" for _ in range(columns)]
        # append the return lists to the game_grid variable
        game_grid.append(row)
        hit_tracker.append(row)
    build_ships(grid_level, game_grid, hit_tracker)
    print_play_area(game_grid, grid_level)


def build_ships(grid_level, game_grid, hit_tracker):
    """
    This function shall take in the grid_level, this value is then used to determine the
    amount of enemy ships to place on the grid, and the particular size of those ships. 
    the location and direction of these ships is handled randomly via the random import.
    These locations are than passed into a seperate function to confirm if they can fit into 
    that particular detination within the game_grid. The function tracks how many ships have been 
    placed and shall continue placing ships until the required figure has been reached. 
    """
    # below set the variables for the amoutn of ships to place and the amount currently placed
    ships_to_place = 0
    enemy_counter = 0

    ships_to_place = 1
    # while the amount of ships placed is NOT equal to the amount of ships to BE placed the
    # script below shall continue to generate random locations for ship placement
    while enemy_counter != ships_to_place:
        heading = random.choice(["north", "south", "east", "west"])
        latitude = random.randint(0, grid_level - 1)
        longitude = random.randint(0, grid_level - 1)
        # the if elif statement below will change the size of ships being placed
        # based on the level input by the user
        if grid_level <= 4:
            ship_size = random.randint(1, 2)
        elif grid_level < 8:
            ship_size = random.randint(1, 4)
        else:
            ship_size = random.randint(1, 5)
        # once the location, size and direction of the ship are determined, these are passed through
        # to a seperate funtion thats uses these values to pinpoint a valid location on the grid for ship placement.
        if place_ship(latitude, longitude, heading, ship_size, grid_level, game_grid, hit_tracker):
            enemy_counter += 1


def place_ship(latitude, longitude, heading, size, grid_level, game_grid, hit_tracker):
    """
    The goal of this function is to take in the overal positon of each ship, randomly generated by the build ship method
    then to check the game_grid lists to see if a ships location is valid, it so this method returns True.

    The first layer of validation will calculate from the randomly generate position, if the ship will fit within the game grid
    if the ship will fit, a second layer of validation will run to check if the given location for the ship is already occupied.
    If a ship already exists in the given location, this method returns false.
    
    If the position is valid, this method returns True and allows for the enemy counter in the build_ship method to increment by 1.
    """
    # the variables below define where to begin 
    # and end the placement of the ships
    lat_start = latitude
    lat_end = latitude + 1
    long_start = longitude
    long_end = longitude + 1 
    # if the randomly generated heading is north
    if heading == "north":
        # if the value for latitude minus the value for the ships size is less than 0
        if latitude - size < 0:
            # returns false to prevent placement off grid
            return False
        # If true will set the starting latitude (for ship placement) of the ship to; the length of the latitude row, minus the size of the ship, plus 1 (emulating a northern direction)
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
    
    # the variable below is set to True and is return by this function if the placement is valid
    position_valid = True

    # for every point of latitude (rows of the grid) within the range randomly generated by the place_ship function
    for lat in range(lat_start, lat_end):
        # for every point of longitude (columns of the grid) within the range randomly generated by the place_ship function
        for long in range(long_start, long_end):
            # if the value assigned to that position is not the ~ symbol 
            if game_grid[lat][long] != "~":
                # change the variable returned by this fuction to false, to prevent placement in the given location
                position_valid = False
                break

    # if the code above has validated the ships position on the grid, position_valid shall be True
    if position_valid:
        # the location of the ship is appended to the ship_location_tracker
        hit_tracker.append([lat_start, lat_end, long_start, long_end])
        # for every point of latitude (rows of the grid) within the range randomly generated by the place_ship function
        for lat in range(lat_start, lat_end):
            # for every point of longitude (columns of the grid) within the range randomly generated by the place_ship function
            for long in range(long_start, long_end):
                # set the value of those cordinates to O to signify the presence of a ship, 
                # this will be replaced with an ~ when the game is printed to the terminal
                game_grid[lat][long] = "O"
                
    # finally if the position was accepted and the values have been updated return true to progress the script
    return position_valid


def print_play_area(game_grid, grid_level):
    debug_mode = True
    # create a string of the alphabet to be used as coordiantes
    # characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if grid_level <= 4:
        print("Two enemies detected! Must be a scouting party.")
    elif grid_level > 4 and grid_level < 8:
        print("Our sonar has detected five enemy vessels!")
        print("")
    elif grid_level >= 8:
        print("Our sonar has detected a fleet of 7 ships!")
    # print("   BOMBS AHOY!")
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
            elif game_grid[row][col] == "X":
                print("X", end=" ")
            else:
                print(game_grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for num in range(len(game_grid)):
        print(str(num), end=" ")
    print("")
    print("")


def main():
    setGridLevel()
    fire_cannons()
    # make_grid()
    # # build_ships()
    # print_play_area()
    

main()