# Global variable for the grid
game_grid = [[]]
# Global variable for the grid size
grid_size = 0
# Global variable for the grid level
grid_level = 0

def setGridLevel(): 
    global grid_level
    grid_level = input(f"Enter a whole number up to 15 to set the grid level\n")
    print(f"You have chosen level {grid_level}. Good Luck!\n")

def printGridLevel():
    print(grid_level)

setGridLevel()
printGridLevel()