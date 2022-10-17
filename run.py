# Global variable for the grid
game_grid = [[]]
# Global variable for the grid size
grid_size = 0
# Global variable for the grid level
grid_level = 0

def setGridLevel(): 
    global grid_level
    
    while True:
        try:
            grid_level = int(input(f"Enter a whole number up to 15 to set the grid level\n"))
        except ValueError:
            print(f"Your input is not valid, please input an integer.\n")
            continue
        else:
            print(f"You chose Level {grid_level}")

            return False

    if grid_level >= 5 and grid_level <= 20:
        print(f"You have chosen level {grid_level}. Good Luck!\n")
    else:
        print(f"Your input is not valid, please input an integer between 5 and 20.\n")
        setGridLevel()

setGridLevel()
