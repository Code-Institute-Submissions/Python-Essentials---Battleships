import itertools
import random
import snoop
import time
import os
from pyfiglet import Figlet

grid_level = 0
game_grid = []
hit_tracker = []
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
enemy_counter = 0
enemy_power_level = 0
power_level = 0
game_start = True
target_located = 0
ammo = 30
game_running = True


def set_grid_level():
    """
    This method is called first in main its purpose is
    to welcome the user to the game and request
    that they input a number between 3 and 10.
    This figure is used to set how difficult
    the game shall be by altering the size of
    the playable grid. The code will validate
    the user input by checking if the figure is
    an integer, equal to or less then 3 and equal
    too or less than 10.
    """
    global grid_level

    while True:
        try:
            # get an integer from 3 to 10 from user
            grid_level = int(input("Enter a number from 3 - 10."))
            print("")

            # check if input is between 3 and 10 if yes call make_grid
            # pass in the captured input
            if grid_level >= 3 and grid_level <= 10:
                print("Setting difficulty...")
                print("")
                make_grid(grid_level)

            else:
                # if not within range, confirm not valid
                # and restart
                print("Your input is not valid, input a number from 3 to 10.")
                print("")
                continue

        # check if input is an integer, if not confirm not valid
        # and restart
        except ValueError:
            print("Your input is not valid, input an integer from 3 to 10.")
            print("")
            continue

        else:
            # if input is valid, print chosen level and
            # return false to close the loop
            print(f"You selected Level {grid_level}. Game Ready.\n")
            return False


def fire_cannons():
    """
    This method is called once the user has input
    a level and the grid has been printed to the
    terminal. The program will request an input
    from the user to confirm the location on the
    grid in which they suspect to find a vessel.
    the input is passed through various layers of
    validation to confirm if it is a valid location
    and to check if that particular location has been
    either fired upon already, is a miss, or a direct
    hit.
    """
    global game_grid
    global power_level
    global target_located
    global ammo
    global game_running

    # creates a loop that shall run until
    # an engame situation occurs
    while game_running:

        # creates a variable for later use
        valid_target = False

        # while valid_target is false the following
        # loop occurs
        while not valid_target:

            # the variable below is used to ensure 
            # that a valid hit to a new target counts
            # for only a 1 point deduction of enemy_power_level
            # without this a bug can cause a 2 point deduction.
            target_located = 0

            # requst an input from user
            print("To make your shot...")
            print(f"Enter a Latitude {characters[0]} - {characters[grid_level-1]}.")
            target = input(f"Then a Longitude from: 0 - {grid_level-1} such as A1:")
            print("")

            # incase of lower case input, convert to uppercase
            target = target.upper()

            # if the user input is less than or equal to 0
            # or greater than 2 in length, invalidate and
            # restart
            if len(target) <= 0 or len(target) > 2:
                print("Misfire!")
                print("Please enter only one alphabetical character...")
                print("Followed by a number e.g. 'A1'")
                print("")
                continue

            # if input length is valid, set lat to input
            # prefix and long to suffix
            lat = target[0]
            long = target[1]

            # if prefix not alphabetical and suffix
            # not numeric, invalidate and restart
            if not lat.isalpha() or not long.isnumeric():
                print("Misfire!")
                print("For the Latitude, please enter a letter...")
                print("For the Longtitude please enter a Number e.g. 'A1'")
                print("")
                continue

            # creates a string from the input prefix
            lat = characters.find(lat)

            # check if the input prefix is a character
            # on the current grid printed. If not
            # invalidate and restart.
            if not (-1 < lat < grid_level):
                print("Misfire!")
                print("That letter is not on the grid!..")
                print("Please enter a valid letter.")
                print("")
                continue

            # creates an integer from the input suffix
            long = int(long)

            # check if the input prefix is a integer
            # on the current grid printed. If not
            # invalidate and restart.
            if not (-1 < long < grid_level):
                print("Misfire!")
                print("The number entered is not valid! Enter a valid number.")
                print("")
                continue

            # if all valid, check if the location has been hit already
            if game_grid[lat][long] in ["#", "X"]:

                # if yes, lower the current ammo count
                ammo = ammo - 1
                print("You've hit this location already Captain! Fire again!")
                print("")

                # then restart
                continue

            # if the input lands on either open water or 
            # an enemy ship, set valid_target to true to
            # close the looping request
            if game_grid[lat][long] in ["~", "O"]:
                valid_target = True

            # clears the terminal to prevent long flowing readouts
            os.system('cls' if os.name == 'nt' else 'clear')

        # once target confirmed valid if open water,
        # annouce a miss and reduce ammo count
        if game_grid[lat][long] == "~":
            ammo = ammo - 1
            print("Captain! Our shot missed! Fire another round!")
            print("")

            # then alter the value for that position in the grid
            # to reflect the miss to the user
            game_grid[lat][long] = "#"

        # once target confirmed valid if enemy ship,
        # annouce a hit and reduce ammo count
        elif game_grid[lat][long] == "O":
            ammo = ammo - 1
            print("That's a direct hit! Well done Captian!")
            print("")
            game_grid[lat][long] = "X"

            # pass the chosen location to a method
            # that will check if the entire ship placed
            # in that location has been hit. if so
            # annouce sunk and increment power_level.
            if track_kills(lat, long):
                print("That's a vessel sunk!")
                print("")
                power_level = power_level + 1

        # finally reprint the grid with the updated
        # hit or miss so the user can track their hits.
        print_play_area(game_grid, grid_level)


def make_grid(grid_level):
    """
    This function will build a sequence of lists which shall then be used,
    later in this script to print the playing area of the game to the terminal.
    """
    global game_grid
    # set rows and columns to the returned grid_level int.
    rows, columns = (grid_level, grid_level)
    # loop through the number of rows
    for _ in range(rows):
        row = ["~" for _ in range(columns)]
        # append the return lists to the game_grid variable
        game_grid.append(row)
    build_ships(grid_level, game_grid)
    print_play_area(game_grid, grid_level)


def build_ships(grid_level, game_grid):
    """
    This function shall take in the grid_level, this value is then used to determine the
    amount of enemy ships to place on the grid, and the particular size of those ships.
    the location and direction of these ships is handled randomly via the random import.
    These locations are than passed into a seperate function to confirm if they can fit into
    that particular detination within the game_grid. The function tracks how many ships have been
    placed and shall continue placing ships until the required figure has been reached.
    """
    # below set the variables for the amoutn of ships to place and the amount currently placed
    global enemy_counter
    global enemy_power_level

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
            ship_size = 1
            ships_to_place = 2
        elif grid_level < 8:
            ship_size = random.randint(1, 3)
            ships_to_place = 5
        else:
            ship_size = random.randint(2, 5)
            ships_to_place = 6
        # once the location, size and direction of the ship are determined, these are passed through
        # to a seperate funtion thats uses these values to pinpoint a valid location on the grid for ship placement.
        if place_ship(latitude, longitude, heading, ship_size, grid_level, game_grid):
            enemy_counter = enemy_counter + 1
            enemy_power_level += ship_size


def place_ship(latitude, longitude, heading, size, grid_level, game_grid):
    """
    The goal of this function is to take in the overal positon of each ship, randomly generated by the build ship method
    then to check the game_grid lists to see if a ships location is valid, it so this method returns True.

    The first layer of validation will calculate from the randomly generate position, if the ship will fit within the game grid
    if the ship will fit, a second layer of validation will run to check if the given location for the ship is already occupied.
    If a ship already exists in the given location, this method returns false.

    If the position is valid, this method returns True and allows for the enemy counter in the build_ship method to increment by 1.
    """
    global hit_tracker
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
        for lat, long in itertools.product(range(lat_start, lat_end), range(long_start, long_end)):
            # set the value of those cordinates to O to signify the presence of a ship,
            # this will be replaced with an ~ when the game is printed to the terminal
            game_grid[lat][long] = "O"

    # finally if the position was accepted and the values have been updated return true to progress the script
    return position_valid


def print_play_area(game_grid, grid_level):
    global game_start
    global enemy_counter
    global power_level
    debug_mode = True
    # create a string of the alphabet to be used as coordiantes
    # characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if game_start:
        if grid_level <= 4:
            print("Two enemies detected! Must be a scouting party.")
        elif grid_level < 8:
            print("Our sonar has detected five enemy vessels!")
        else:
            print("Our sonar has detected a fleet of 7 ships!")
        print("")
        game_start = False
    else:
        tracker = enemy_counter - power_level
        if tracker <= 1:
            print("The battle is ours!")
        elif tracker < 3:
            print("Their forces are weak!")
        elif tracker == 3:
            print("The battle could be over soon, brace!")
        elif tracker >= 4:
            print("It's not over yet, stay frosty!")
        else:
            print("The enemy approaches, ready the cannons!")
        print("")
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
        print(num, end=" ")
    print("")
    print("")


def track_kills(lat, long):
    global hit_tracker
    global game_grid

    for hit in hit_tracker:
        lat_start = hit[0]
        lat_end = hit[1]
        long_start = hit[2]
        long_end = hit[3]

        if lat_start <= lat <= lat_end and long_start <= long <= long_end:
            ship_located()

            for r, c in itertools.product(range(lat_start, lat_end), range(long_start, long_end)):
                if game_grid[r][c] != "X":
                    return False

    return True


def ship_located():
    global enemy_power_level
    global enemy_counter
    global target_located
    global ammo

    if target_located == 0:
        enemy_power_level = enemy_power_level - 1
        print(enemy_power_level)
        target_located = target_located + 1
    if enemy_power_level == 0:
        win_game()
    elif ammo == 0 and enemy_power_level > 0:
        loose_game()


def win_game():
    global game_running

    game_running = False

    os.system('cls' if os.name == 'nt' else 'clear')

    f = Figlet(font='slant')
    print(f.renderText("VICTORY"))

    while True:
        try:
            replay = input(f"Well done for beating Level: {grid_level}\n\nWould you like to play again? Y/N:\n")
            replay = replay.upper()

            if replay == "Y":
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system("python run.py")
                exit()
            elif replay == "N":
                exit()

            else:
                print(f"Your input is not valid, please input Y to play again or N to leave the game.\n")
                continue

        except ValueError:
            print(f"Your input is not valid, please input either Y or N.\n")
            continue

        else:
            # if input is valid, print chosen level and return false to close the while loop
            print(f"Reloading...\n")
            return False


def loose_game():
    global game_running

    os.system('cls' if os.name == 'nt' else 'clear')

    f = Figlet(font='slant')
    print(f.renderText("GAME OVER"))

    while True:
        try:
            replay = input(f"You failed level: {grid_level}\n\nWould you like to play again? Y/N")
            replay = replay.upper()

            if replay == "Y":
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system("python run.py")
                exit()
            elif replay == "N":
                exit()

            else:
                print(f"Your input is not valid, please input Y to play again or N to leave the game.\n")
                continue

        except ValueError:
            print(f"Your input is not valid, please input either Y or N.\n")
            continue

        else:
            # if input is valid, print chosen level and return false to close the while loop
            print(f"Reloading...\n")
            return False


def main():
    set_grid_level()
    fire_cannons()


main()
