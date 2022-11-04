 # Welcome to BLACKBEARD's BATTLESHIPS!
Welcome to Blackbeard's Battleships a Python terminal based battleships game deployed via the Code Institute mock Terminal on Heroku.

The game is one player, users will battle against the computer. Users can chose from several difficulty options ranging from 3 to 10 with grid sizes starting at 3x3 then incrementing by 1x1 to 10x10 at max. The size range, and number of ships will also increase with higher levels. Positions, directions and ship lengths are all randomised each game. 

Users can input coordinates from the grid in a 'CharacterNumber' format such as A1. These coordinates are validated and an outcome is determined. Ammo is limited to 30 shots per game, if users reach 0 before sinking all enemy ships they will loose. Users must sink all enemy ships to win.

The game features a main menu, where users can navigate through an instruction manual explaining the games usage along with a legend. The game contains a variety of built in cheat codes with various effects to compliment gameplay, these are detailed in the content below. 

Refer to Wikipedia for the History of [Battleships](https://en.wikipedia.org/wiki/Battleship_(game))


![Responsive](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/responsive-mockup.png)

## How to Play 

- The game begins with an intro menu, requesting an input of either 'HELP' or 'RUN'. If the user inputs 'HELP' the instruction manual shall load with some breif in-game help and a legend of the symbols used. If the user inputs 'RUN' the game shall start. The next screen requests another input, this time an integer from 3 to 10, validation is present throughout all input areas within the module, and will catch any inputs deemed invalid. This number is used to determin the playing area of the game. Entering 4 for example, will produce a 4x4 grid, entering 10 will produce a 10x10 grid. Higher numbers will also effect the range to randomised ship length and the number of indidual targets to generate on the grid.

- Users have a limited amount of shots available, these are displayed in a clear message beneath the game grid itself and is updated with every shot made (provided it is not a 'misfire' AKA invalidated input). Users will be penalised, loosing 1 ammo if you miss a target open water, users will also be penalised if a user targets the same location twice (same input as as previous input). Users will NOT be penalised if you enter an invalid input. Your current ammo count can be increased through the means of two cheatcodes built-in to the game, 'TENSHOTS' and 'FIVESHOTS' which when input, will increase ammo by either 10 or 5.

- The goal is to sink completely, all of the enemies ships to win. Run out of ammo before and you will loose. Helpful messages will appear above the grid to alert users when a ship has been completely destroyed. Messages that take the form of vague indications towards the remaining amount of ships will also be printed above the grid. 

- When the user has chosen a valid level, The grid is populated with enemy ships and printed to the terminal, the game shall then request a target on the grid. The input for this request takes the from of first an alphabetical character, then a number such as 'A1'. Cheat codes can also be entered when the computer requests a target, when input correctly, a message shall appear with the text 'Cheat Activated' and a description of the effect. At any time when an input is requested from the user, enter 'EXIT' to close the game.

- The user will be notified when either a Victory or Game Over scneario occurs, confirmation of what level they either failed or completed shall appear in the terminal. Then a request from the user to play again or leave the game.

### Legend:

- Green colored 'X': Relates to an succesful hit in that grid position.
- Red colored '#': Relates to a previous target in that grid position.
- Blue colored '~': Relates to open water in that grid position.
- Cyan colored 'O': Relates to an enemy ship in that grid position.

### Existing Features

- __Intro Menu__

  - When the script first runs, the run_intor method is called, printing a welcome page to the terminal complete with a titled render in an illustrative font. Users are then prompted for an input of either 'HELP' or 'RUN'. HELP will clear the terminal output and print the game manual (covered below). RUN will jump straight into the game itself, where the user is prompted for a level (covered below) 
  
  - The benefit of this feature to users is in welcoming them to the experience, familiarising themselves with the basic input functions of the game. It allows users to first consult an instruction manual in-game, and returning users to jump straight in.   

A                          |  B                        
:-------------------------:|:-------------------------:
![Intro Menu](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart.png)|![Intro Menu](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart-b.png)

- __Game Manual__

  - The game manual is a second feature created by the run_intro method. It features a brief explanantion of the games features and operation, this areas inputs come complete with validation. This area leads to the legend (covered below) and gives users an option to either return to the intro menu, or jump directly into the game having consulted the manual first. The games cheat features are referenced here also.
  
  - The benefit this feature has is clear in the information it provides to the user, the games operation is covered here, the cheat features are referenced here and a legend is located here also. This feature would be invaluable to a user not familiar with the game and its functions.

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![Game Manual](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![Game Manual](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![Game Manual](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)

- __Legend__

  - This feature is contained within the game manual. It shows the symbols that are used to represent various components of the game along with a explanation of what the symbol represents, such as a green X chosen to respresent a succesful hit. A small but important feature. 
  
  - The benefit of this feature to users is found in the information it provides, familiarising the user with the symbols that appear on the game grid. This feature, along with the intro menu and the game manual are of most benefit to new users, providing all the neccesary information to play the game properly. They would likely not be of much benefit to returning users. 

A                          |  B                        
:-------------------------:|:-------------------------:
![Legend](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart.png)|![Legend](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart-b.png)

- __Numerous difficulty levels__ 

  - The playing area could be viewed as the primary feature of the site, its in this section that players will ccreat their paterns, the heart of the game itself is contain within this tool, as without it the game could not operate. This tool is responsive, and interactive and encourages the game play loop. 
  
  The styles of the Player One (seen in column A) and Player Two (seen in column B) windows in the PVP Game Type are different to illustrate the change in control. New games are also activated via this tool.
  - As mentioned above, this tool is the heart of the game itself, no matter which game type you chose, whether player one or player two, you will be acquainted with this tool. Without it the gameplay loop would not exist and players would not be able to operate the games functions outside of the main menu. Therefore this tool could be seen to be the most valuable feature of all. 

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![Numerous difficulty levels](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![Numerous difficulty levels](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![Numerous difficulty levels](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)

- __In Game hints__

  - The score chart will appear in both the PVP and P VS Computer game types, in PVP (seen in column A) Player One and Player Two can use this scoreboard to change and set their player name for the game. These names can be carried into new games. The scoreboard also efficiently records and reflects the scores in points for the two players. 
  
  In the P VS Computer (seen in column B) game type, only the name for player one can be altered, the scoreboard will instead reflect the scores for the Computer
  - This is a crucial tool for the gameplay. This records the winners of each of the three rounds in each overall game, then awards points up to a maximum of three to the winning party. Players can predetermine the end goal, such as first to 10 points, this scoreboard allows for these points to be recorded. 
  
A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![In Game hints](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![In Game hints](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![In Game hints](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)

- __The Grid__

  - This box will display the input chosen by both player one (P1) and player two (P2) to allow users to check the results themselves, in the P VS Computer game type, players can see their own choices alongside the patern randomly generated by the computer (PC). 
  - This tool allows the players to compare the paterns or to compare against the computer to reinforce the results of the game. 

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![The Grid](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![The Grid](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![The Grid](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)

- __Ammo Counter__

  - The message center will display messages at different stages of the game, if the hidden cheat option is activated, messages are flagged here, images of these messageds are found further in this document. 
  
  Including the nuke alerts, the winners of rounds 1, 2 and 3 are declared through these messages, the game will use the chosen player names and declared who wins the point or if the round is a draw. 
  - This tool notifys players of certain actions taking place within the gameplay, and of the results of each round, without this players can use the scoreboard or compare the paterns via the tool explained above. Theses messages add an extra Quality of Life layer to the game.  

![Ammo Counter](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/message.png)

- __Input with validation__

  - At the bottom of the game area are two buttons, one of them sits inside the playing window and bares the text 'Play again' (seen in column A), this option will fire up the next game whilst carrying the previous scores and chosen player names forward. 
  
  The other button 'Main Menu' (seen in column B) shall reset the game and return players to the landing screen, main game menu.
  - The play again button will give players the option to carry on the scoring, perhaps they are playing first to 10 points? A maximum of 3 points can be awarded per round so this option carries forward any chosen player names and current scores into fresh games.
  - The main menu button will allow players to return to the main menu, whilst resetting the player names, current scores and chosen paterns. Effectively resetting the game itself whilst providing straightforward site navigation. 

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)
D                          |  E                        | F
:-------------------------:|:-------------------------:|:-------------------------:
![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)


- __Cheat Options__

  - This area of the site features a game manual for the Player vs Player game type, it explains the various functions and concepts within the game, such as the patern comparison, the scoring, how to operate the game, it explains how to carry over scores and set the player names.  
  - This guide covers the PVP game type and its operation in entriety which is invaluable to thos finding difficulty understanding the game at first, this would likely be of most use to an older audience of those less versed in digital technology.

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-one.png)|![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-two.png)|![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-three.png)
D                          |  E                        | F
:-------------------------:|:-------------------------:|:-------------------------:
![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-one.png)|![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-two.png)|![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-three.png)


- __GAME OVER / VICTORY Screens__

  - This area of the site features a game manual for the Player vs Computer game type, it explains the various functions and concepts within the game, such as the patern comparison, the scoring, how to operate the game, it explains how to carry over scores and set the player name.  
  - This guide covers the P VS Computer game type and its operation in entriety which is invaluable to thos finding difficulty understanding the game at first, this would likely be of most use to an older audience of those less versed in digital technology.

A                          |  B                        
:-------------------------:|:-------------------------:
![Legend](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart.png)|![Legend](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart-b.png)

- __Play again with validation/confirmation__

  - This button acts as a call-to-action. featured at the bottom of both game manuals, this button shall start the relevant game type without needing to return to the main menu.  
  - Players who chose first to review the rules of the game and its functions will be pleased to see they do not need to reset the game or make unnecesary clicks and can begin a game with no roadblocks to move around. 

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![Play again with validation/confirmation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-one.png)|![Play again with validation/confirmation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-two.png)|![Play again with validation/confirmation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-three.png)

### Potential features to Implement

- An expansion to a two-board style, where the user can chose and place their own ships, which will be randomly targetted by the computer.
- An option to set a user name, although this would not likely provide much benefit to the game.


# Testing 

- Tested with numerous invalid inputs, the game contains various input requests, integers, strings etc have been tested and correctly invalidated. 
- Tested extensively in IDE terminal with consistent desired results. 
- Tested via the Heroku mock Terminal to ensure appropriate formating of text, and efficient operation. 

## Validator Testing 

### Tested with [PEP8](https://pep8.readthedocs.io/en/release-1.7.x/intro.html) Validator within workspace environment
INSTALLATION: '$ pip install pep8' USAGE: '$ pep8 --first run.py' OR '$ pep8 --statistics -qq run.py' OR '$ pep8 --show-source --show-pep8 run.py'
No Errors remaining. 

### Tested wit [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.htmlhttps://pycodestyle.pycqa.org/en/latest/intro.html) Validator within workspace environment
INSTALLATION: '$ pip install pycodestyle' USAGE: '$ pycodestyle --first run.py' OR '$ pycodestyle --statistics -qq run.py' OR '$ pycodestyle --show-source --show-pep8 run.py'
No Errors remaining.

### Tested wit [PyLint](https://pylint.pycqa.org/en/latest/) Validator within workspace environment
INSTALLATION: '$ pip install pylint' USAGE: Intergrated into IDE 

## Disregarded PyLint Messages 

Below are various message that appeared in the 'Problems' window of my Gitpod Workspace and relate to the run.py file. All real problems and issues with the scirpt were identified and addressed through the validators above. However, these messages are still present in the script today. Through my testing and investigation I feel it is appropriate to disregard these messages. The particular message and the justification to disregard are recorded below.

 ### f-string is missing placeholders / f-string is not using any interpolated values.
   - I am taking advantage of the '\n' line break through the use of the f-strings
     therefore I have chosen to disregard this message. 

 ### Using the Global Statement. .
   - To ensure that all methods used within the module work correctly and free from any errors
     (That I have been able to discover through testing), some methods require the use of global
     statements.

 ### Constant does not conform to UPPER_CASE naming style.
   - This relates to the names given to my methods, I have chosen to use lower_case naming conventions.
     and so chose to disregard this message.
   
 ### Variable does not conform to snake_case naming style.
   - this relates to a variable 'f' used to store a PyFiglet font. I have chosen lower_case naming conventions for variables
     and so chose to disregard this message. 
    
 ### Consider using enumerate instead of iterating with range and len.
   - I tested and experimented with using enumerate within the method this message relates to and the effects were undesired
     from my perspective and experience in testing, iterating with range and len produced the desired result.  
    
 ### Unncesary parens after 'not' keyword.
   - Like the message above, i experimented with removing and altering the parens this message relates to and like the issue above,
     the effects produce were not wanted, and the parens that remain in the existing script were deemed neccesary for the desired outcome. 

### Unfixed Bugs

- There are no known bugs, clear through extensive testing currently within the game.

## Deployment

- The code was deployed to the Code Institutes mock Terminal on Heroku. The steps to deploy are as follows: 
  - Fork or clone this repository. Or create a project via the [CI Python Template](https://github.com/Code-Institute-Org/python-essentials-template) 
  - Create a new app via Heroku, name the app something descriptive. 
  - From the settings page add the following build packs in this order: 1st Python, 2nd node.js.
  - Add a Config Var with the following details: KEY = PORT, VALUE = 8000.
  - Selecte the 'Deploy' tab chose the 'GitHub' dpeloyment method and connect with the relevant GitHub repo.
  - It is avisable to chose the 'Manual Deploy' method, selecting the 'Main' branch then selcting 'Deploy'
  - Wait for the terminal to complete and deploy the app. 

The live link can be found here - [BLACKBEARD's BATTLESHIPS](https://whlw27.github.io/JavaScript-Essentials---Rock-Paper-Scissors-Spock/).


## Credits  

### Helpful information

- Additional guidance on Python was found on [W3 Schools](https://www.w3schools.com/).
- Additional self-lead projects and study on Python was found on [Codecademy](https://www.codecademy.com/learn) via the PRO subscription.

### Python Libraries used

- [Random](https://docs.python.org/3/library/random.html) - randint, .choice, randrange. were used to genreate random ship lengths, random directions and placements for ships, and by the RANDO cheat to determin a random location to target. 
- [Time](https://docs.python.org/3/library/time.html) - .sleep() was used in a variety of locations in the module, particularly to delay print messages and certain steps within methods. 
- [Snoop](https://pypi.org/project/snoop/) - The '@snoop' decorator was used extensively during testing when the script ran to large for a servie such as PythonTutor, snoop printed the code steps and return values of the relevant method to the terminal, allowing for me to debug issues deep into the games logic. 
- [PyFiglet](https://pypi.org/project/pyfiglet/0.7/) - Figlet was used to render some print text in the terminal through an illustrative font style, adding some visual elements to the text. 
- [OS](https://docs.python.org/3/library/os.html) - used to clear the terminal at various points within the game logic, in an IDE this will clear the terminal output, with heroku this will move the text currently printed in the terminal out of sight and above new text to be printed.
- [Itertools](https://docs.python.org/3/library/itertools.html) -.product was used to refactor a statement iterating through lists into a faster and more code effficient solution by locating the cartesian product of the given iterators.  

