# Used to refactor a statement
import itertools

# used to generate random information
# for ship placements
import random

# used to delay certain elements of the script
import time

# used to clear the terminal readout
# in various stages of the script
import os

# used to render illustrative text to the terminal.
from pyfiglet import Figlet

# The following variables are used or altered by
# more than 1 of the methods below and are required
# to be iun global scope.
grid_level = 0
game_grid = []
hit_tracker = []
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
enemy_counter = 0
enemy_power_level = 0
power_level = 0
game_start = True
target_located = 0
ammo = 3
game_running = True
result = ""
debug_mode = False


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
    # Must access the grid_level global variable.
    global grid_level

    while True:
        try:
            # get an integer from 3 to 10 from user
            grid_level = int(input("Enter a number from 3 - 10:"))
            print("")

            # check if input is between 3 and 10 if yes call make_grid
            # pass in the captured input
            if grid_level >= 3 and grid_level <= 10:
                print("Setting difficulty...")
                print("")
                make_grid()

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


def make_grid():
    """
    This method is called once the user has chosen a level
    its purpose is to build a sequence of lists which shall
    then be appended to the game_grid for later printing.
    when the grid has been made, this method calls the
    build_ships method to assing boat positions. Then
    calls print_game_grid.
    """
    # set rows and columns to the returned grid_level int.
    rows, columns = (grid_level, grid_level)

    # add an ~ to every positon across the rows
    # and columns of the grid.
    for _ in range(rows):
        row = ["~" for _ in range(columns)]

        # append the return lists to the game_grid
        game_grid.append(row)

    # once grid has been created call the method to
    # build and place ships on grid
    build_ships()

    # once ships have been placed, call method to print
    # the grid to the terminal.
    print_play_area()


def build_ships():
    """
    This function shall take in the grid_level, this value is
    then used to determine the amount of enemy ships to place
    on the grid, and the particular size of those ships. The
    location and direction of these ships is handled randomly
    via the random import. These locations are than passed into
    a seperate function to confirm if they can fit into that
    particular detination within the game_grid. The function
    tracks how many ships have been placed and shall continue
    placing ships until the required figure has been reached.
    """
    # Must access the following
    # global variables.
    global enemy_counter
    global enemy_power_level

    # create a variable for the amount
    # of enemy ships to place on grid.
    ships_to_place = 1

    # while the amount of ships placed is NOT equal
    # to the amount of ships to BE placed the
    # script below shall continue to generate
    # random locations for ship placement
    while enemy_counter != ships_to_place:
        heading = random.choice(["north", "south", "east", "west"])
        latitude = random.randint(0, grid_level - 1)
        longitude = random.randint(0, grid_level - 1)

        # the if elif statement below will change
        # the size of ships being placed
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

        # once the location, size and direction of the ship
        # are determined, these are passed through
        # to the place_ship method thats uses these
        # values to pinpoint a valid location on the
        # grid for ship placement.
        if place_ship(latitude, longitude, heading, ship_size):
            enemy_counter = enemy_counter + 1
            enemy_power_level += ship_size


def place_ship(latitude, longitude, heading, size):
    """
    The goal of this function is to take in the positon of each ship,
    randomly generated by the build ship method, to check the game_grid
    lists values to see if a the ship generated will fit on the grid itself
    and not overlap with a currently placed vessel, if so
    the position information is stored in the hit_tracker variable
    and values are changed within the game_grid this method then
    returns True. If the position overlaps or lands off the grid
    itself, it is considered not valid and this method returns false
    """
    # the variables below define where to begin
    # and end the placement of the ships
    lat_start = latitude
    lat_end = latitude + 1
    long_start = longitude
    long_end = longitude + 1

    # if the randomly generated heading is north
    if heading == "north":

        # if the Latitude minus the size of the ship
        # is less than 0.
        if latitude - size < 0:

            # returns false to prevent placement off grid
            return False

        # if the value for latitude minus the value for
        # the ships size is above 0 will set the starting
        # latitude (for ship placement) of the ship to;
        # the length of the latitude row, minus the size
        # of the ship, plus 1 (emulating a northern direction)
        lat_start = latitude - size + 1

    # if the randomly generated heading is east
    elif heading == "east":

        # if the longitude plus the size of the ship
        # is greater than or equal to grid_level.
        if longitude + size >= grid_level:

            # returns false to prevent placement off grid
            return False

        # if the value for longitude plus the value for
        # the ships size is greater than or equal to
        # the grid_level, will set th end longitude
        # (for ship placement) of the ship to;
        # the longitude plus the size of the ship
        # (emulating an eastern direction)
        long_end = longitude + size

    # if the randomly generated heading is south
    elif heading == "south":

        # if the latitude plus the size of the ship
        # is greater than or equal to grid_level.
        if latitude + size >= grid_level:

            # returns false to prevent placement off grid
            return False
        lat_end = latitude + size

    # if the randomly generated heading is west
    if heading == "west":

        # if the longitude minus the size of the ship
        # is less than 0.
        if longitude - size < 0:

            # returns false to prevent placement off grid
            return False

        # if the value for longitude minus the value for
        # the ships size is less than 0, will set the starting
        # longitude (for ship placement) of the ship to;
        # the longitude minus the size of the ship + 1
        # (emulating a western direction)
        long_start = longitude - size + 1

    # the variable below is set to True
    # to confirm a valid placement on grid
    position_valid = True

    # The code below then takes then values
    # passed through the functions above and
    # uses them to dictate the range that shall
    # be iterated through within the game_grid lists
    # to confirm if the value assigned to those positions
    # is an ~ symbolising open water. Provided all positions
    # are clear, the position is considered valid on grid, and
    # valid by not overlapping a current vessel.
    for lat in range(lat_start, lat_end):

        # for every point of longitude (columns of the grid)
        # within the range randomly generated by the place_ship function
        for long in range(long_start, long_end):

            # check the value assigned to that location.
            if game_grid[lat][long] != "~":

                # If a ships detected in this position,
                # change the below variable to False and break
                # from the loop to return position_valid.
                position_valid = False
                break

    # if the code above has validated the ships position
    # on the grid, the code nested below shall trigger.
    if position_valid:

        # the location details of the ship are
        # first appended to the hit_tracker designed
        # to track ship positions.
        hit_tracker.append([lat_start, lat_end, long_start, long_end])

        # The position of the ship will then be used
        # to dictate what positions of the game_grid list
        # to assign a new value to, that being a O. to
        # track the ships location on the grid itself.
        for lat, long in itertools.product(
                range(lat_start, lat_end),
                range(long_start, long_end)):
            game_grid[lat][long] = "O"

    # finally return either true of false
    # dependant on conditions above.
    return position_valid


def print_play_area():
    """
    This method is called first once the game grid has
    been created and populated with enemy ships. It is
    later called by the fire_cannons method to reprint
    a fresh grid to the terminal with a record of the
    users shots/misses. Its purpose is to read the value
    of the game_grid variable. Then print a Letter, a border
    then a row of ~ symbols to symbolise the targetable area
    it will detect if a ship has been hit and print an X.
    it will detect if a shot has missed and print an #.
    a cheat has been hidden within this method, debug_mode
    which when activated will reveal the position of ships
    on the grid with a O.
    """
    # Must access the following
    # global variables.
    global game_start

    # The code below will read the grid level chosen by
    # the user and print a statement when the grid is printed
    # for the first time, indicating how many enemies are on
    # the grid.
    if game_start:
        if grid_level <= 4:
            print("Two enemies detected! Must be a scouting party.")
        elif grid_level < 8:
            print("Our sonar has detected five enemy vessels!")
        else:
            print("Our sonar has detected a fleet of 7 ships!")
        print("")
        # The line below ensures that the print statments above only
        # occur on the first printing of the grid.
        game_start = False

    else:
        # The code below keeps track of the current number
        # of enemy vessels still on the grid. It shall print
        # clue statements as an indictation of the users progress.
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

    # Begin printing the rows of the Grid, start with
    # the alphabetical character beginning with A, and
    # follow with a border |. Do this for every row of the grid.
    for row in range(len(game_grid)):
        print(characters[row], end="| ")

        # Then print the collumns of the grid, this is where ships
        # are located and shots are made.
        for col in range(len(game_grid[row])):

            # The code below will check to see if debug_mode
            # is True, if so the ship locations as they are placed
            # are revealed when the grid is printed to the terminal
            # this allows assessors to confirm their placement.
            if game_grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    # If debug is flase, the standard grid is
                    # printed and the ships are hidden.
                    print("~", end=" ")

            # If a ship has been hit, the grid is printed with
            # an X to notify the user.
            elif game_grid[row][col] == "X":
                print("X", end=" ")
            else:
                print(game_grid[row][col], end=" ")
        print("")

    # The code below will print a row of numbers beneath
    # the game grid, beginning at 0, the combination of
    # letter and number are used to pinpoint targets on
    # the grid.
    print("  ", end=" ")
    for num in range(len(game_grid)):
        print(num, end=" ")
    print("")
    print("")

    print(f"You have {ammo} shots remaining.\n")


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
    # must be able to read from and change the
    # following globals.
    global power_level
    global target_located
    global ammo
    global debug_mode
    global result

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
            print("To make your shot", end='')
            print(f" enter a Latitude {characters[0]} -", end='')
            print(f" {characters[grid_level-1]}.", end='')
            print(" Then a Longitude from 0 - ", end='')
            target = input(f"{grid_level-1} such as A1:\n")

            # incase of lower case input, convert to uppercase
            target = target.upper()

            if target == "CHEATMODE":
                time.sleep(0.5)
                debug_mode = True
                if debug_mode:
                    print("Cheat activated! All ships have been revealed!")
                    continue

            if target == "FIVESHOTS":
                time.sleep(0.5)
                ammo = ammo + 5
                print("Cheat activated! Ammo increased!")
                continue

            if target == "TENSHOTS":
                time.sleep(0.5)
                ammo = ammo + 5
                print("Cheat activated! Ammo increased!")
                continue

            if target == "DAVEYJONES":
                time.sleep(0.5)
                print("You fled the battle!")
                time.sleep(1)
                result = "loose"
                end_game()

            if target == "KRAKENTIME":
                time.sleep(0.5)
                print("The Kraken has swallowed the enemy whole!")
                time.sleep(1)
                result = "win"
                end_game()

            # if the user input is less than or equal to 0
            # or greater than 2 in length, invalidate and
            # restart
            if len(target) < 2 or len(target) > 2:
                print("Misfire!")
                print("Please enter only one alphabetical character", end='')
                print(f" followed by a number e.g. 'A1'\n")
                continue

            # if input length is valid, set lat to input
            # prefix and long to suffix
            lat = target[0]
            long = target[1]

            # if prefix not alphabetical and suffix
            # not numeric, invalidate and restart
            if not lat.isalpha() or not long.isnumeric():
                print("Misfire!")
                print("For the Latitude, please enter a letter", end='')
                print(f" for the Longtitude please enter a Number e.g. 'A1'\n")
                continue

            # creates a string from the input prefix
            lat = characters.find(lat)

            # check if the input prefix is a character
            # on the current grid printed. If not
            # invalidate and restart.
            if not (-1 < lat < grid_level):
                print("Misfire!")
                print("That letter is not on the grid!", end='')
                print(f" Please enter a valid letter.\n")
                continue

            # creates an integer from the input suffix
            long = int(long)

            # check if the input prefix is a integer
            # on the current grid printed. If not
            # invalidate and restart.
            if not (-1 < long < grid_level):
                print("Misfire!")
                print("The number entered is not valid!", end='')
                print(f" Enter a valid number.\n")
                continue

            # if all valid, check if the location has been hit already
            if game_grid[lat][long] in ["#", "X"]:

                # if yes, lower the current ammo count
                ammo = ammo - 1
                print("You've hit this location already", end='')
                print(f"Captain! Fire again!\n")
                if ammo <= 0:
                    result = "loose"
                    end_game()

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
            print(f"Captain! Our shot missed! Fire another round!\n")
            if ammo <= 0:
                result = "loose"
                end_game()

            # then alter the value for that position in the grid
            # to reflect the miss to the user
            game_grid[lat][long] = "#"

        # once target confirmed valid if enemy ship,
        # annouce a hit and reduce ammo count
        elif game_grid[lat][long] == "O":
            ammo = ammo - 1
            print(f"That's a direct hit! Well done Captian!\n")
            game_grid[lat][long] = "X"

            # pass the chosen location to a method
            # that will check if the entire ship placed
            # in that location has been hit. if so
            # annouce sunk and increment power_level.
            if track_kills(lat, long):
                print(f"That's a vessel sunk!\n")
                power_level = power_level + 1

        # finally reprint the grid with the updated
        # hit or miss so the user can track their hits.
        print_play_area()


def track_kills(lat, long):
    """
    This method fires on the condition that the user
    has performed a direct hit on an enemy vessel.
    its purpose is to iterate through the track ship
    positions in the hit_tracker global, checking if
    they match against the users input. if so, the
    ship_located method is called. On the condition
    that the targetted ship's size is above 0, This
    method will also confirm if the other sections
    of the targetted ship have been hit, to confirm
    a sunken vessel.
    """
    # Assigns the list values from the hit_tracker global
    # to variables
    for hit in hit_tracker:
        lat_start = hit[0]
        lat_end = hit[1]
        long_start = hit[2]
        long_end = hit[3]

        # The code below will confirm if the users input
        # matches a target on the hit tracker.
        # and call the ship_located method if true.
        if lat_start <= lat <= lat_end and long_start <= long <= long_end:
            ship_located()

            # the code below will check the list
            # positions surrounding the targeted
            # location, to confirm if the connected
            # sections of the ship currently
            # targeted have all been hit.
            for r, c in itertools.product(
                    range(lat_start, lat_end),
                    range(long_start, long_end)):
                # If the list positions connected to the
                # targeted ship are not X signifying a
                # previous direct hit, return false.
                if game_grid[r][c] != "X":
                    return False

    return True


def ship_located():
    """
    This method is called on the condition that the users input
    matches the location of a freshly targeted enemy ship.
    its purpose is to check the current ammo count for the user,
    to check and alter the current enemy_power_level, to call the
    method to win or loose the game if conditions are met, or run
    code to reduce the value asssigned to the enemy_power_level global.
    which is neccesary for the game to accurately call a victory or game
    over.
    """
    # Must access the following
    # global variables.
    global result
    global enemy_power_level
    global target_located

    # The code below will only run if the value
    # of the target_located variable is 0.
    # This ensures the indented code runs only
    # once per confirmed hit on target.
    if target_located == 0:

        # Will reduce the value of enemy_power_level by 1
        # to track for a winning situation.
        enemy_power_level = enemy_power_level - 1

        # Increments target_located by 1 to prevent
        # running twice per hit target.
        target_located = target_located + 1

    # If the value of enemy_power_level is equal to 0
    # call the win_game method.
    if enemy_power_level == 0:
        result = "win"
        end_game()

    # The code below will run if the value of the ammo
    # global is 0 whilst the enemy_power_level is simultaneously
    # greater than 0. This is to ensure that the users final shot
    # can still win the game if it sinks the final target.
    elif ammo <= 0 and enemy_power_level > 0:
        result = "loose"
        end_game()


def end_game():
    """
    This method is called on the condition that the
    enemy_power_level has reached 0 by the time the
    ammo has reached 0. This would be a winning situation.
    the purpose of this method is to congradulate the user
    then as if they wish to play again. the code shall validate
    their input, on the condition the user wants to exit the
    program, a second input shall request confirmation and validate
    the input given. This method will either restart the program
    or exit the program.
    """
    # Must be able to alter the game_running global
    global game_running

    # Stop the loop requesting user input if a target.
    game_running = False

    # clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    if result == "win":
        # Using the PyFiglet Library, print VICTORY rendered
        # # in an alternate font
        f = Figlet(font='slant')
        print(f.renderText("VICTORY"))

    else:
        # Using the PyFiglet Library, print GAME OVER rendered
        # # in an alternate font
        f = Figlet(font='slant')
        print(f.renderText("GAME OVER"))

    # Create a loop to request a user input
    # and validate said input
    while True:
        try:
            if result == "win":
                print(f"Well done for beating Level: {grid_level}\n\n")
            else:
                print(f"You failed Level: {grid_level}\n\n")

            # request a Y to play agian or an N to exit
            replay = input(f"Would you like to play again? Y/N:\n")
            replay = replay.upper()

            # If Y is input, clear the terminal and re run the program
            if replay == "Y":
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system("python run.py")
                exit()

            # If input is N close the program.
            elif replay == "N":

                # first start a loop to confirm if the
                # user wants to exit
                confirm = True
                while confirm:
                    try:

                        # Ask if sure and request a Y/N input once more.
                        print("Are you sure you want", end='')
                        confirm = input(" to close the game? Y/N: ")
                        confirm = confirm.upper()

                        # If Y close the game.
                        if confirm == "Y":
                            exit()

                        # if N close the loop
                        elif confirm == "N":
                            confirm = False

                        # If invalid input, notify of an error
                        # and ask again.
                        else:
                            print(f"Your input is not valid,", end='')
                            print(" please input Y to play ", end='')
                            print(f"again or N to leave the game.\n")
                            continue

                    # The code below does not appear to run
                    # through testing various inputs. I have
                    # included it to address any inputs i may
                    # not have considered.
                    except ValueError:
                        print("Your input is not valid")
                        print(f", please input either Y or N.\n")
                        continue

            # If invalid input, notify of an error
            # and ask again.
            else:
                print(f"Your input is not valid,", end="")
                print(" please input Y to play", end='')
                print(f" again or N to leave the game.\n")
                continue

        # The code below does not appear to run
        # through testing various inputs. I have
        # included it to address any inputs i may
        # not have considered.
        except ValueError:
            print(f"Your input is not valid, please input either Y or N.\n")
            continue


def main():
    set_grid_level()
    fire_cannons()


main()
