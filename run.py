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
            grid_level = int(input(f"Enter a whole number between 5 and 20 to set the difficulty.\nThe number input shall set the size of the games grid.\n"))
            if grid_level >= 5 and grid_level <= 20:
                print("Setting difficulty...")
            else:
                print(f"Your input is not within the range, please input an number between 5 and 20.\n")
                continue
        except ValueError:
            print(f"Your input is not valid, please input an integer, e.g. a whole number between 5 and 20.\n")
            continue
        else:
            print(f"You selected Level {grid_level}. Game Ready.")
            return False


setGridLevel()
