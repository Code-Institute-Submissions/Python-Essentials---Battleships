"""
Welcome to Blackbeard's Battleships. A Python Terminal battelships
game. The game is one player, users will battle against the
computer. Users can chose from several difficulty options ranging
from 3 to 10 with grid sizes starting at 3x3 then incrementing by
1x1 to 10x10 at max. The size range, and number of ships will also
increase with higher levels. Positions, directions and ship lengths
are all randomised each game. Users can input coordinates from the
grid in a 'CharacterNumber' format such as A1. These coordinates are
validated and an outcome is determined. Ammo is limited to 30 shots per
game, if users reach 0 before sinking all enemy ships they will loose.
Users must sink all enemy ships to win

Cheat codes:
RANDO: Generates a randomised target location.
CHEATMODE: Reveals the enemy ships on the grid.
TENSHOTS: Ammo increased by 5.
FIVESHOTS: Ammo increased by 5.
DAVEYJONES: Instant Game Over.
KRAKENTIME: Instant Victory.

Legend:
Green colored 'X': Relates to an succesful hit in that grid position.
Red colored '#': Relates to a previous target in that grid position.
Blue colored '~': Relates to open water in that grid position.
Cyan colored 'O': Relates to an enemy ship in that grid position.
"""
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
# to be in global scope.
grid_level = 0
game_grid = []
hit_tracker = []
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
enemy_counter = 0
enemy_power_level = 0
power_level = 0
game_start = True
game_running = True
result = ""
debug_mode = False


def run_intro():
    """
    The purpose of this method is to print a welcome page
    acting like a main menu for the game. From here users
    can access an instruction manual of sorts, containing
    a detailed explanation of the games features. Users can also
    head straight into the game from via this method. The code
    prints various statements, passing some as arguments to
    external methods for formatting and printing.
    The method contains various validation layers as users move
    through the instructions.
    """
    # Set colors of text to be printed.
    print("\033[1;31;40m")

    # setup figlet fonts.
    f = Figlet(font='xttyb')

    print(f"Welcome to...\n")

    os.system('cls' if os.name == 'nt' else 'clear')

    # then print the intro terminal
    print(f.renderText(" BLACKBEARD's"))
    print(f.renderText(" BATTLESHIPS"))

    # Required variable to close the below while loop.
    stage_one = True

    while stage_one:
        try:
            # Request user input.
            print("\033[0;37;40mInput 'HELP' to read the game manual.")
            print(f"Input 'RUN' to start the game\033[1;32;40m\n")
            user_call = input("INPUT: ")

            # incase of lower case input, convert to uppercase
            user_call = user_call.upper()

            # clear terminal.
            os.system('cls' if os.name == 'nt' else 'clear')

            # if HELP begin printing the instruction manual.
            if user_call == "EXIT":
                stage_one = False
                print("Thank you for playing!")
                print("")
                print("Leaving game...")
                time.sleep(0.75)
                exit()

            if user_call == "HELP":
                # close the parent loop.
                stage_one = False

                print(f.renderText(" BLACKBEARD's"))
                print(f.renderText(" BATTLESHIPS"))

                print(f"\033[1;34;40mHow to Play:\033[0;37;40m\n")
                print("\033[0;37;40m When starting the game", end="")
                run_manual_two(
                    " the computer shall request",
                    " a Number from 3 to 10.\n",
                    " This number is used to determin")

                print(f" the playing area of the game.\n")
                print(f" Entering 4 for example, will produce a 4x4 grid.\n")
                run_manual_one(
                    " Higher numbers will also effect the size",
                    " and number of enemy ships on the grid.\n")

                print(f" You have a limited amount of shots available.\n")
                run_manual_two(
                    " You will be penalised ",
                    "if you miss of shoot a target twice.\n",
                    " You will NOT be penalised ")

                print(f"if you enter an invalid input.\n")
                run_manual_one(
                    " Your current ammo count shall ",
                    " be displayed beneath the grid.\n")

                # Required variable to close the below while loop.
                stage_two = True

                while stage_two:
                    try:
                        print("Input 'N' to continue or 'Q'", end="")
                        print(f" to leave...\033[1;32;40m\n")
                        next_slide = input("INPUT: ")
                        next_slide = next_slide.upper()

                        os.system('cls' if os.name == 'nt' else 'clear')

                        if next_slide == "N":

                            stage_two = False

                            print(f.renderText(" BLACKBEARD's"))
                            print(f.renderText(" BATTLESHIPS"))

                            print(f"\033[1;34;40mContinued...\033[0;37;40m\n")
                            run_manual_two(
                                "\033[0;37;40m Sink completely, ",
                                "all of the enemies ships to win.\n",
                                " Run out of ammo before ")

                            print(f"and you will loose.\n")
                            print(" You will be alerted when ", end="")
                            print(f"ships have been destroyed.\n")
                            run_manual_one(
                                " Hints towards remaining amount of ",
                                "ships will be printed above the grid.\n")

                            print(" When you have input the level ", end="")
                            run_manual_two(
                                ", the game shall request ",
                                "a target on the grid.\n",
                                " Input first an ")

                            run_manual_two(
                                "alphabetical character",
                                ", then a number such as 'A1'\n",
                                " Cheat codes can be entered when ")

                            run_manual_one(
                                "the computer requests ",
                                "your target input.\n")
                            print(" At anytime enter ", end="")
                            print(f"'EXIT' to leave the game.\n")

                            print(f"\033[1;34;40mLegend:\033[0;37;40m\n")
                            print("Green colored ", end="")
                            print("'\033[1;32;40mX\033[0;37;40m': ", end="")
                            print("Relates to a succesful ", end="")
                            print("hit in that grid position.")
                            print("Red colored ", end="")
                            print("'\033[1;31;40m#\033[0;37;40m': ", end="")
                            print("Relates to a previous ", end="")
                            print("target in that grid position.")
                            print("Blue colored ", end="")
                            print("'\033[1;34;40m~\033[0;37;40m': ", end="")
                            print("Relates to open water", end="")
                            print(" in that grid position.")
                            print("Cyan colored ", end="")
                            print("'\033[1;36;40mO\033[0;37;40m': ", end="")
                            print("Relates to an enemy ", end="")
                            print(f"ship in that grid position.\n")

                            stage_three = True

                            while stage_three:
                                try:
                                    print("Input 'QUIT' to return", end="")
                                    print(" to the main menu or ", end="")
                                    print("'MORE' for detailed instructions.")
                                    print("Otherwise input ", end="")
                                    print("'START' to play", end="")
                                    print(f" the game.\033[1;32;40m\n")
                                    next_slide = input("INPUT: ")
                                    next_slide = next_slide.upper()

                                    os.system(
                                        'cls' if os.name == 'nt' else 'clear'
                                        )

                                    if next_slide == "MORE":
                                        r = open(
                                            "instruction.txt",
                                            "r",
                                            "t",
                                            encoding="utf-8"
                                            )
                                        instruction = r.read()
                                        print(instruction)

                                    if next_slide == "QUIT":
                                        stage_three = False
                                        os.system(
                                            'cls' if os.name == 'nt' else
                                            'clear'
                                            )
                                        run_intro()
                                        break
                                    if next_slide == "START":
                                        stage_three = False
                                        set_grid_level()
                                        break
                                    if next_slide == "EXIT":
                                        stage_three = False
                                        print("Thank you for playing!")
                                        print("")
                                        print("Leaving game...")
                                        time.sleep(0.75)
                                        exit()
                                    else:
                                        if not stage_three:
                                            break
                                        print("Input not recognised", end="")
                                        print(f", please try again\n")
                                        continue
                                except ValueError():
                                    print(f"\031[0;32;40mYour", end="")
                                    print(" input is not ", end="")
                                    print(f"valid. Please try again.\n")
                                    print("")
                                    continue
                                else:
                                    break
                        if next_slide == "EXIT":
                            stage_two = False
                            print("Thank you for playing!")
                            print("")
                            print("Leaving game...")
                            time.sleep(0.75)
                            exit()

                        if next_slide == "Q":
                            stage_two = False
                            os.system('cls' if os.name == 'nt' else 'clear')
                            run_intro()
                            break
                        else:
                            if not stage_two:
                                break
                            print(f"Input not recognised, please try again\n")
                            continue
                    except ValueError():
                        print("\031[0;32;40mYour input is", end="")
                        print(f" not valid. Please try again.\n")
                        print("")
                        continue
                    else:
                        break

            # If RUN start the game
            if user_call == "RUN":
                stage_one = False
                set_grid_level()
                break

            # If EXIT leave the game
            if user_call == "EXIT":
                stage_one = False
                print("Thank you for playing!")
                print("")
                print("Leaving game...")
                time.sleep(0.75)
                exit()
            else:
                if not stage_one:
                    break
                print(f"Input not recognised, please try again\n")
                continue
        except ValueError():
            print(f"\031[0;32;40mYour input is not valid. Please try again.\n")
            print("")
            continue
        else:
            break


def run_manual_one(arg0, arg1):
    """
    This method was created to improve the code quality of the
    run_intro function. By removing print statements from above
    and passing them through to this function as arguments. Its
    purpose is to print the arguments passed to the terminal.
    applying relevant formatting in the process. This takes two
    arguments.
    """
    print(arg0, end="")
    print(f"{arg1}")

    print("")


def run_manual_two(arg0, arg1, arg2):
    """
    This method was created to improve the code quality of the
    run_intro function. By removing print statements from above
    and passing them through to this function as arguments. Its
    purpose is to print the arguments passed to the terminal.
    applying relevant formatting in the process. This takes three
    arguments.
    """
    print(arg0, end="")
    print(f"{arg1}")
    print(arg2, end="")


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
    while True:
        try:
            # get an integer from 3 to f10 from user
            set_grid_level.grid_level = int(input(
                "\033[0;37;40mEnter a number from 3 - 10: \033[1;32;40m"))
            print("")

            # check if input is between 3 and 10 if yes call make_grid
            # pass in the captured input
            if (
                set_grid_level.grid_level >= 3 and
                set_grid_level.grid_level <= 10
                    ):
                print("\033[0;37;40mSetting difficulty...")
                print("")
                make_grid()

            else:
                # if not within range, confirm not valid
                # and restart
                print("\033[1;31;40m")
                print("Your input is ", end="")
                print("not valid, input a number from 3 to 10.")
                print("")
                continue

        # check if input is an integer, if not confirm not valid
        # and restart
        except ValueError:
            print("\033[1;31;40m")
            print("Your input is not ", end="")
            print("valid, input an integer from 3 to 10.")
            print("")
            continue

        else:
            # if input is valid, print chosen level and
            # return false to close the loop
            print("\033[0;37;40mYou selected \033[0;32;40mLevel ", end="")
            print(f"{set_grid_level.grid_level}\033[0;37;40m. Game Ready.\n")
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
    rows, columns = (set_grid_level.grid_level, set_grid_level.grid_level)

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
        latitude = random.randint(0, set_grid_level.grid_level - 1)
        longitude = random.randint(0, set_grid_level.grid_level - 1)

        # the if elif statement below will change
        # the size of ships being placed
        # based on the level input by the user
        if set_grid_level.grid_level <= 4:
            ship_size = 1
            ships_to_place = 3
            build_ships.ammo = 10

        elif set_grid_level.grid_level < 8:
            ship_size = random.randint(1, 3)
            ships_to_place = 5
            build_ships.ammo = 20

        else:
            ship_size = random.randint(2, 5)
            ships_to_place = 7
            build_ships.ammo = 30

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
        if longitude + size >= set_grid_level.grid_level:

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
        if latitude + size >= set_grid_level.grid_level:

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
        if set_grid_level.grid_level <= 4:
            print("\033[1;36;40m3 enemies ", end="")
            print("detected! Must be a scouting party.")
        elif set_grid_level.grid_level < 8:
            print("\033[1;36;40mOur sonar ", end="")
            print("has detected 5 enemy vessels!")
        else:
            print("\033[1;36;40mOur sonar ", end="")
            print("has detected a fleet of 7 ships!")
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
            print("\033[1;32;40mThe battle is ours!")
        elif tracker < 3:
            print("\033[1;36;40mTheir forces are weak!")
        elif tracker == 3:
            print("\033[1;34;40mThe battle could be over soon, brace!")
        elif tracker >= 4:
            print("\033[1;35;40mIt's not over yet, stay frosty!")
        else:
            print("\033[1;31;40mThe enemy approaches, ready the cannons!")
        print("")

    # Begin printing the rows of the Grid, start with
    # the alphabetical character beginning with A, and
    # follow with a border |. Do this for every row of the grid.
    print("\033[1;34;40m")
    for row in range(len(game_grid)):
        print(characters[row], end="| \033[0;34;40m")

        # Then print the collumns of the grid, this is where ships
        # are located and shots are made.
        for col in range(len(game_grid[row])):

            # The code below will check to see if debug_mode
            # is True, if so the ship locations as they are placed
            # are revealed when the grid is printed to the terminal
            # this allows assessors to confirm their placement.
            if game_grid[row][col] == "O":
                if debug_mode:
                    print("\033[1;36;40mO\033[0;34;40m", end=" ")
                else:
                    # If debug is flase, the standard grid is
                    # printed and the ships are hidden.
                    print("\033[0;34;40m~", end=" ")

            # If a ship has been hit, the grid is printed with
            # an X to notify the user.
            elif game_grid[row][col] == "X":
                print("\033[1;32;40mX\033[0;34;40m", end=" ")
            else:
                print(game_grid[row][col], end=" ")
        print("\033[1;34;40m")

    # The code below will print a row of numbers beneath
    # the game grid, beginning at 0, the combination of
    # letter and number are used to pinpoint targets on
    # the grid.
    print("  ", end=" ")
    for num in range(len(game_grid)):
        print(num, end=" ")
    print("")
    print("")

    print("\033[0;31;46mYou have \033[1;33;46m", end="")
    print(f"{build_ships.ammo}\033[0;31;46m shots remaining.\033[0;31;40m\n")


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
    global debug_mode

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
            fire_cannons.target_located = 0

            # requst an input from user
            print("\033[0;37;40mTo make your shot", end='')
            print(f" enter a Latitude \033[1;37;40m{characters[0]} -", end='')
            print(f" {characters[set_grid_level.grid_level-1]}\033[0;37;40m.")
            print("Then a Longitude from \033[1;37;40m0 - ", end='')
            print(f"{set_grid_level.grid_level-1}", end="")
            print(f"\033[0;37;40m such as A1.\033[1;32;40m \n")
            target = input("INPUT: ")

            # incase of lower case input, convert to uppercase
            target = target.upper()

            # CHEATCODE: Will fire on a random location of the grid.
            if target == "RANDO":
                print(f"\033[0;37;40mWhat's all this then?\n")
                print(f"\033[1;31;40mHANGFIRE!\n")
                print("\033[0;37;40mCareful mateys!", end="")
                print(" This cannon could fire anywhere!")
                time.sleep(2.25)
                random_letter = chr(
                    random.randrange(97, 97 + set_grid_level.grid_level - 1)
                    )
                random_letter = random_letter.upper()
                random_number = random.randrange(
                    0, set_grid_level.grid_level - 1
                    )
                target = random_letter+str(random_number)
                print("")
                print("Looks like it landed on \033[1;32;40m" + target)
                print("")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')

            # Method to exit the game.
            if target == "EXIT":
                print("Thank you for playing!")
                print("")
                print("Leaving game...")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()

            # CHEATCODE: Will activate debug_mode causing
            # enemy ships to appear on the grid.
            if target == "CHEATMODE":
                time.sleep(0.5)
                debug_mode = True
                if debug_mode:
                    print("\033[1;37;40mCheat activated!", end="")
                    print("\033[0;37;40m All ships have been revealed!")
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_play_area()
                    continue

            # CHEATCODE: Will increase current ammo count by 5.
            if target == "FIVESHOTS":
                time.sleep(0.5)
                build_ships.ammo = build_ships.ammo + 5
                print("\033[1;37;40mCheat activated!", end="")
                print("\033[0;37;40m Ammo increased by \033[1;37;40m5!")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print_play_area()
                continue

            # CHEATCODE: Will increase current ammo count by 10.
            if target == "TENSHOTS":
                time.sleep(0.5)
                build_ships.ammo = build_ships.ammo + 10
                print("\033[1;37;40mCheat activated!", end="")
                print("\033[0;37;40m Ammo increased by \033[1;37;40m10!")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print_play_area()
                continue

            # CHEATCODE: Will raise Davey jones to
            # collect his debt, causing a GAME OVER.
            if target == "DAVEYJONES":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;40m")
                f = Figlet(font='slant')
                print(f.renderText("TIME TO PAY"))
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                print("\033[0;31;40mDavey Jones ", end="")
                print("has arrived to collect your soul!")
                time.sleep(1.5)
                fire_cannons.result = "loose"
                end_game()

            # CHEATCODE: Will raise a kraken to
            # wipe out the grid and cause a Victory.
            if target == "KRAKENTIME":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;40m")
                f = Figlet(font='radical_')
                print(f.renderText("KRAKEN"))
                print(f.renderText("ATTACK"))
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                print("\033[0;31;40mThe Kraken has swallowed the enemy whole!")
                time.sleep(1.5)
                fire_cannons.result = "win"
                end_game()

            # if the user input is less than or equal to 0
            # or greater than 2 in length, invalidate and
            # restart
            if len(target) < 2 or len(target) > 2:
                print("\033[1;31;40mMisfire!")
                print("Please enter only one alphabetical character", end='')
                print(f" followed by a number e.g. 'A1'\n")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print_play_area()
                continue

            # if input length is valid, set lat to input
            # prefix and long to suffix
            lat = target[0]
            long = target[1]

            # if prefix not alphabetical and suffix
            # not numeric, invalidate and restart
            if not lat.isalpha() or not long.isnumeric():
                print("\033[1;31;40mMisfire!")
                print("For the Latitude, please enter a letter", end='')
                print(f" for the Longtitude please enter a Number e.g. 'A1'\n")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print_play_area()
                continue

            # creates a string from the input prefix
            lat = characters.find(lat)

            # check if the input prefix is a character
            # on the current grid printed. If not
            # invalidate and restart.
            if not (-1 < lat < set_grid_level.grid_level):
                print("\033[1;31;40mMisfire!")
                print("That letter is not on the grid!", end='')
                print(f" Please enter a valid letter.\n")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print_play_area()
                continue

            # creates an integer from the input suffix
            long = int(long)

            # check if the input prefix is a integer
            # on the current grid printed. If not
            # invalidate and restart.
            if not (-1 < long < set_grid_level.grid_level):
                print("\033[1;31;40mMisfire!")
                print("The number entered is not valid!", end='')
                print(f" Enter a valid number.\n")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print_play_area()
                continue

            # if all valid, check if the location has been hit already
            if game_grid[lat][long] in ["\033[1;31;40m#\033[0;34;40m", "X"]:

                # if yes, lower the current ammo count
                build_ships.ammo = build_ships.ammo - 1
                print("\033[1;31;40mYou've hit this location already ", end='')
                print(f"Captain! Fire again!\n")
                if build_ships.ammo <= 0:
                    fire_cannons.result = "loose"
                    end_game()

                # then restart
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print_play_area()
                continue

            # if the input lands on either open water or
            # an enemy ship, set valid_target to true to
            # close the looping request
            if game_grid[lat][long] in ["~", "O"]:
                valid_target = True

            # clears the terminal to prevent long flowing readouts
            # os.system('cls' if os.name == 'nt' else 'clear')

        # once target confirmed valid if open water,
        # annouce a miss and reduce ammo count
        if game_grid[lat][long] == "~":
            build_ships.ammo = build_ships.ammo - 1
            print("\033[0;31;40mCaptain! Our ", end="")
            print(f"shot missed! Fire another round!\n")
            if build_ships.ammo <= 0:
                fire_cannons.result = "loose"
                end_game()
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

            # then alter the value for that position in the grid
            # to reflect the miss to the user
            game_grid[lat][long] = "\033[1;31;40m#\033[0;34;40m"

        # once target confirmed valid if enemy ship,
        # annouce a hit and reduce ammo count
        elif game_grid[lat][long] == "O":
            build_ships.ammo = build_ships.ammo - 1
            print(f"\033[0;32;40mThat's a direct hit! Well done Captian!\n")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            game_grid[lat][long] = "X"

            # pass the chosen location to a method
            # that will check if the entire ship placed
            # in that location has been hit. if so
            # annouce sunk and increment power_level.
            if track_kills(lat, long):
                print(f"\033[0;35;40mThat's a vessel sunk!\n")
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
    global enemy_power_level

    # The code below will only run if the value
    # of the target_located variable is 0.
    # This ensures the indented code runs only
    # once per confirmed hit on target.
    if fire_cannons.target_located == 0:

        # Will reduce the value of enemy_power_level by 1
        # to track for a winning situation.
        enemy_power_level = enemy_power_level - 1

        # Increments target_located by 1 to prevent
        # running twice per hit target.
        fire_cannons.target_located = fire_cannons.target_located + 1

    # If the value of enemy_power_level is equal to 0
    # call the win_game method.
    if enemy_power_level == 0:
        fire_cannons.result = "win"
        end_game()

    # The code below will run if the value of the ammo
    # global is 0 whilst the enemy_power_level is simultaneously
    # greater than 0. This is to ensure that the users final shot
    # can still win the game if it sinks the final target.
    elif build_ships.ammo <= 0 and enemy_power_level > 0:
        fire_cannons.result = "loose"
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

    if fire_cannons.result == "win":
        illustrate("\033[1;32;40m", 'radical_', "VICTORY")
    else:
        illustrate("\033[1;31;40m", 'slant', "GAME OVER")
    # Create a loop to request a user input
    # and validate said input
    while True:
        try:
            if fire_cannons.result == "win":
                print("\033[0;32;40mWell done for ", end="")
                print("completing Level: \033[1;32;40m", end="")
                print(f"{set_grid_level.grid_level}\n\n")
            else:
                print("\033[0;31;40mYou failed Level: ", end="")
                print(f"\033[1;31;40m{set_grid_level.grid_level}\n\n")

            # request a Y to play agian or an N to exit
            print("\033[0;37;40mWould you like to", end="")
            replay = input(f" play again? Y/N:\033[1;32;40m\n")
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
                        print("\033[0;37;40mAre you sure you want", end='')
                        confirm = input(
                            " to close the game? Y/N:\033[0;32;40m ")
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
                            print("\033[0;31;40mYour input", end='')
                            print(" is not valid,", end="")
                            print(" please input Y to play ", end='')
                            print(f"again or N to leave the game.\n")
                            continue

                    # The code below does not appear to run
                    # through testing various inputs. I have
                    # included it to address any inputs i may
                    # not have considered.
                    except ValueError:
                        print("\033[0;31;40mYour input is not valid")
                        print(f", please input either Y or N.\n")
                        continue

            # If invalid input, notify of an error
            # and ask again.
            else:
                print(f"\033[0;31;40mYour input is not valid,", end="")
                print(" please input Y to play", end='')
                print(f" again or N to leave the game.\n")
                continue

        # The code below does not appear to run
        # through testing various inputs. I have
        # included it to address any inputs i may
        # not have considered.
        except ValueError:
            print("\033[0;31;40mYour input is not ", end="")
            print(f"valid, please input either Y or N.\n")
            continue


def illustrate(arg0, font, arg2):
    """
    This method was created to improve the code quality of the
    end_game method. It takes the ANSI color code, the figlet
    font style and the text to print as arguments. its purpose
    is to render illustrative typography in a certain color to
    the terminal.
    """
    # Print the ANSI to set colors.
    print(arg0)

    # Setup and print the figlet text.
    f = Figlet(font=font)
    print(f.renderText(arg2))


def main():
    """
    This function is called first when the script runs,
    its prupose is to call the methods needed to operate
    the game.
    """
    run_intro()
    fire_cannons()


main()
