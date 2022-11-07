 # Welcome to BLACKBEARD's BATTLESHIPS!
Welcome to Blackbeard's Battleships a Python terminal based battleships game deployed via the Code Institute mock Terminal on Heroku.

The game is one player, users will battle against the computer. Users can chose from several difficulty options ranging from 3 to 10 with grid sizes starting at 3x3 then incrementing by 1x1 to 10x10 at max. The size range, and number of ships will also increase with higher levels. Positions, directions and ship lengths are all randomised each game. 

Users can input coordinates from the grid in a 'CharacterNumber' format such as A1. These coordinates are validated and an outcome is determined. Ammo is limited to 30 shots per game, if users reach 0 before sinking all enemy ships they will loose. Users must sink all enemy ships to win.

The game features a main menu, where users can navigate through an instruction manual explaining the games usage along with a legend. The game contains a variety of built in cheat codes with various effects to compliment gameplay, these are detailed in the content below. 

Refer to Wikipedia for the History of [Battleships](https://en.wikipedia.org/wiki/Battleship_(game))


![Responsive](https://github.com/WHLW27/Python-Essentials---Battleships/blob/main/assets/images/responsivemockup.png)

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


## Project Goals
- The project is a simple take on the Battleships game concept. The player only needs to consider their oponents ships and their current avaiable ammo count.
- The game has a variety of difficulty options, gird sizes range from 3x3 to 10x10, 3 enemy ships at the lowest level and 7 at the highest. The sizes of the ships are randomised but generally will be larger the higher the level. 
- You win the game by sinking all ships on the grid before your ammo count reaches 0. 

## User Experience
- The user experience will be comfortable adn familiar to those acustomed to battlehsips. Color is featured extensively to highlight important information to players providing a good QOL. Commands are simple with straightforward inputs. Cheat codes have been included to enhance the overall experience. 

### Existing Features

- __Intro Menu__

  - When the script first runs, the run_intor method is called, printing a welcome page to the terminal complete with a titled render in an illustrative font. Users are then prompted for an input of either 'HELP' or 'RUN'. HELP will clear the terminal output and print the game manual (covered below). RUN will jump straight into the game itself, where the user is prompted for a level (covered below) 
  
  - The benefit of this feature to users is in welcoming them to the experience, familiarising themselves with the basic input functions of the game. It allows users to first consult an instruction manual in-game, and returning users to jump straight in.   

A                          |  B                        
:-------------------------:|:-------------------------:
![Intro Menu](https://github.com/WHLW27/Python-Essentials---Battleships/blob/main/assets/images/mainmenu.png)|![Intro Menu](https://github.com/WHLW27/Python-Essentials---Battleships/blob/main/assets/images/mainmenuvalid.png)

- __Game Manual__

  - The game manual is a second feature created by the run_intro method. It features a brief explanantion of the games features and operation, this areas inputs come complete with validation. This area leads to the legend (covered below) and gives users an option to either return to the intro menu, or jump directly into the game having consulted the manual first. The games cheat features are referenced here also.
  
  - The benefit this feature has is clear in the information it provides to the user, the games operation is covered here, the cheat features are referenced here and a legend is located here also. This feature would be invaluable to a user not familiar with the game and its functions.

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![Game Manual](https://github.com/WHLW27/Python-Essentials---Battleships/blob/main/assets/images/manual-one.png)|![Game Manual](https://github.com/WHLW27/Python-Essentials---Battleships/blob/main/assets/images/manual-two.png)|![Game Manual](https://github.com/WHLW27/Python-Essentials---Battleships/blob/main/assets/images/detailed-manual.png)

- __Legend__

  - This feature is contained within the game manual. It shows the symbols that are used to represent various components of the game along with a explanation of what the symbol represents, such as a green X chosen to respresent a succesful hit. A small but important feature. 
  
  - The benefit of this feature to users is found in the information it provides, familiarising the user with the symbols that appear on the game grid. This feature, along with the intro menu and the game manual are of most benefit to new users, providing all the neccesary information to play the game properly. They would likely not be of much benefit to returning users. 

A                          |  B                        
:-------------------------:|:-------------------------:
![Legend](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart.png)|![Legend](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart-b.png)

- __Numerous difficulty levels__ 

  - The difficulty ranges from Low with a 3x3 grid and 3 targets on the grid, to medium with a 5x5 Grid and 5 targets. Then increasing up to High, starting from grid sizes of 8x8 to a max of 10x10 featuring 7 targets. Ammo count will range from 10 at 3x3 (meaning it is only possible to fail 3x3 by making several mistake such as targeting locations twice), to 20 from level 5 and increasing to 30 at mixmum. (This count can be effected by the cheat codes.)
  
  - This feature gives the game lots of replayability, with challenges increasing in difficulty. There is an option available to younger audiences or those with less skill with the 3x3 giving a fun opportunity to test the game and its features with room to make a mistake without an serious consequence. There is an option for players seeking a challenge, with 10x10, and an ammo count of 30 covering only 30% of the potential target locations, tactical or logical thinking is required. Mistakes are expensive and pressure is much more apparent. The game despite the fixed difficulties also gives users the chance to manipulate the difficulty via the ingame cheats, increasing ammo availablilty at higher levels to bring the pressure down. 

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![Numerous difficulty levels](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![Numerous difficulty levels](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![Numerous difficulty levels](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)

- __In Game hints__

  - At the beginning stage of the game, as the grid has been printed for the 1st time, depending on the level input for the grid size, a short hint indicative of the number of enemy ships on the grid will appear above the grid itself. The text is descriptive and follows the theme or naval piracy I decided to aim for. These messages make clear the games 'personality' to the user and provide them with the exact number of ships they need to sink. To avoid confusion further into the gameplay this message disapears after the first valid target has been hit. 

  They are then replaced with a second type of message, giving a vague hint of how many ships there may curently be still unsank, these messages are intentionally vague to provide the game with some extra challenge, but I feel they are descriptive enough to benefit the users decisions ingame. 

  A third type of message shall appear to notify the user when they have succesfully hit all connected sections or a target, AKA sank a ship on the grid. 
  
 - This message center of sorts provides teh user with multiple layers of information, aluding to the challenge ahead, their current progress in game and of their achievments, the messages are not permanent to keep the terminal output clean and readable. This feature is not particularly neccesary beyond stating the number of targets, but it benefits the experience by increasing the interaction between the user and the game itself. The game responds to the user and strengthens their feelings of control over the games outcome, while providing additional oppotunities to give the game some character. 
  
A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![In Game hints](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![In Game hints](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![In Game hints](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)

- __The Grid__

  - The heart of the game itself, the Grid is the most important feature of the game. It is what defines the gameplay, it acts as a record sheet, tracking succesful hits, misses and potential target locations. It acts as an extension of the games legend, showing symbols relative to each object. It acts as your target locator or recticle of sorts. It tracks game progress. The grid can vary in size from 3x3 to 10x10 with 9 potential targets and up to 100. By entering the cheat code 'CHEATMODE' users cna reveal all ships on the grid, indicated by the character 'O'. 

  In normal gameplay, potential targets are marked by a '~', direct hits on target with a 'X' and misses are marked with a '#'. The alphabetical characters on the left side and the number beneath will vary depending on the grid size but begin at 'A' and '0'.
  
  - This feature is invaluble to users, it provide a facility to track their progress through the game, gives a QOL feature by clearly indicating missed targets or succesful hits which the user can then use to guess their next shot with more logical accuracy. The grid can be manipulated by the player through cheat codes, giving users more control. Color is featured heavily in this area to provide a visual treat to the user. 

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![The Grid](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![The Grid](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![The Grid](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)

- __Ammo Counter__

  - Beneath the Games grid when this had been printed to the terminal, a message shall appear with the text 'You have X shots remaining' where 'X' marks the current ammo count. This game uses the current avaiable ammo count to determine the outcome of the game, the ammo avaiablity contributes a large part of the games challenge at higher diffuclty levels. This count begins at 10 with a 3x3 grid, raising to 20 at 5x5 and 30 from grid sizes of 8 and above. This count can be manipulate in game by the user through the avaibale TENSHOTS and FIVESHOTS cheat codes.

- Without this feature the user would find the game play much more difficult at higher levels, its abesence overall would be a nuisance to the user given the games logic relies on the ammo value. This feature helps users track their progress and draws their attention towards how many chances they have remaining to beat the level which in some circumstance can add to the pressure of thec challenge. 

![Ammo Counter](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/message.png)

- __Input with validation__

  - Validation is featured in every situation where an input is requested from the user, messages will appear to notify the user of invalid inputs and the program shall request the particular input again, and shall continue to do so until a valid input has been provided. 

  Most inputs are looking for a simple string response and will notify the user of what partiuclar word the program is looking for in the invalid input warnings. 

  The method to set the games grid level will produce different error messages depending in the data input, too long of an input will produce a different message to an input made entirely of integers or an input of unrecognised characters. Examples of the warnings users might experience can be veiwed in the table below.
  
  - This feature provides the user with some security in knowing they cannot drastically damage their experience through invalid inputs, or have the gameplay be efffected by any glitch or bug as a result of thier error. They can play the game at their own pace. Each warning the user might experience is descriptive and explains what situation may have occured, such as landing a hit on the same spot twice. The warnings give the user the information neccesary to understand what will be valid.

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)
D                          |  E                        | F
:-------------------------:|:-------------------------:|:-------------------------:
![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-one.png)|![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-two.png)|![Input with validation](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/pvc-three.png)


- __Cheat Options__

  - The game features several built-in cheats. They can be input when the program is requesting a user input for the target. The effects range from humorous to exploitative. There are options for increasing the current ammo, options to instantly call a GAME OVER or VICTORY, a Randomised target feature and a God mode style cheat that reveals all enemy ships on the grid. 
  
  - These cheat features give the game some extra fun in game, and provide users with the option to manipulate the stakes at higher difficulty levels. This provides a level of freedom to the user along with the chance to choose the difficulty through the grid size. This supliments the loss of freedom from my decision to focus on a 1 Grid concept by contrast to the typical 2 Grid concept. 
  - Additionaly these features where beneficial to me as the developer in the games testing process and should be of benefit to an assessor for similar reasons. 
- 
  ### Cheat codes:
  - RANDO: Generates a randomised target location.
  - CHEATMODE: Reveals the enemy ships on the grid.
  - TENSHOTS: Ammo increased by 5.
  - FIVESHOTS: Ammo increased by 5.
  - DAVEYJONES: Instant Game Over.
  - KRAKENTIME: Instant Victory. 

A                          |  B                        | C
:-------------------------:|:-------------------------:|:-------------------------:
![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-one.png)|![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-two.png)|![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-three.png)
D                          |  E                        | F
:-------------------------:|:-------------------------:|:-------------------------:
![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-one.png)|![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-two.png)|![Cheat Options](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/nuke-three.png)


- __GAME OVER / VICTORY Screens__

  - This screen will display either GAME OVER or VICTORY, rendered illustratively in a graphical font style. These screens pay homage to the classic GAME OVER screens we gamers are all acustomed too. They provide a clear statement, a conclusion, and a visual treat to the user. 
  
  - This feature makes the results of the game clear to the user and opens the gates for them to continue the gameplay. The screens are bright, eye catching and (considering the graphical  limitations of a game of this kind) visually apppealing. Although the feature is simple, its neccesary to provide users with an adequate, flowing gaming experience, by providing the penultimate stage of the gameplay loop. 

A                          |  B                        
:-------------------------:|:-------------------------:
![Legend](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart.png)|![Legend](https://github.com/WHLW27/JavaScript-Essentials---Rock-Paper-Scissors-Spock/blob/main/assets/images/readme/score-chart-b.png)

- __Play again with validation/confirmation__

  - This screen is rather simple and follows from either the GAME OVER or VICTORY screens, an user input is requested, a simple 'N' to close the game or 'Y' to restart the program and thus play again. Inputs in this location are validated and the program shall request input until a valid input has been received. Shoudl the user input 'N' the program shall request a second input as confirmation to exit, incase of accidental inputs. This input is again a 'Y' or 'N' request with validation. 'Y' in this circumstance shall confirm the users decision to exit the program. 
   
  - The benefit this feature has to users is by providing an option to loop the game logic and to extend their play session further. Or provides them with a 'ritual' to draw their play session to an end. Quiting is still an action every user will take and this screen gives them the facility to do so with the closure they have 'Completed' their experience.   

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

 ### Too many lines in module.
   - Docstrings at interpreted by the compiler however single line comments are not, removing all single line comments from the module would bring the line count comfortably below the 1000 standard. I feel it is appropriate to disregard the single line comments. 

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

## Setting up the Repo

- Log in to GitHub and nvaigate to the [CI Python Template](https://github.com/Code-Institute-Org/python-essentials-template) .
- Select the 'Use this template' button.
- Choose a name and description for the repo.
- Select the 'Creat repository from template' button.

## Forking

- Sign in to Github and go to [BLACKBEARD's BATTLESHIPS](https://github.com/WHLW27/Python-Essentials---Battleships).
- Select the 'Fork' button at the top right hand side of the webpage.
- Choose a name and description for the fork.
- Select the 'Create Fork' button.

## Cloning

- Sign in to Github and go to [BLACKBEARD's BATTLESHIPS](https://github.com/WHLW27/Python-Essentials---Battleships).
- Above the file table click the ‘code’ button.
- Several options are avaliable, HTTPS, SSH and GitHub CLI, make a choice and select the 'Copy to clipboard' button next to the URL.
- Open git bash.
- Type ‘git clone’ and then paste the URL you copied. Press Enter.
- For more information read the topic [Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Deployment

- The code was deployed to the Code Institutes mock Terminal on Heroku. The steps to deploy are as follows: 
  - Fork or clone this repository. Or create a project via the [CI Python Template](https://github.com/Code-Institute-Org/python-essentials-template) 
  - If your requirements.txt file has not changed you can skip this step. Otherwise, in your terminal type 'pip3 freeze > requirements.txt' then save and push the changes.
  - Sign in to Heroku.com
  - Create a new app via Heroku, name the app something descriptive. 
  - From the 'Settings' tab find the 'Config Vars' section and click the 'Reveal Config Vars' button.
  - Add a Config Var with the following details: KEY = PORT, VALUE = 8000.
  - (The next step applies only if your project requires a creds.json file) In the field for 'KEY' enter the value 'CREDS' in all capitals. In the field for 'VALUE' copy and paste the entire contents of your creds.json file from your project. Then click 'Add'.
  - From the settings page add the following build packs by selecting the 'Add Buildpacks' button. Add packs in this order: 1st Python, 2nd node.js.
  - Selecte the 'Deploy' tab chose the 'GitHub' deployment method and connect with the relevant GitHub repo.
  - It is avisable to chose the 'Manual Deploy' method, selecting the 'Main' branch then selcting 'Deploy'
  - If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.
  - Wait for the terminal to complete and deploy the app. 

The live link can be found here - [BLACKBEARD's BATTLESHIPS](https://blackbeards-battleships.herokuapp.com/).


## Credits  

- Code Institute for the Python Template used. 

### Code resources and guidance.

- Additional guidance on Python was found on [W3 Schools](https://www.w3schools.com/).
- Additional guidance on Python was found on [GeeksforGeeks](https://www.geeksforgeeks.org/).
- Additional guidance on Python was found on [Stack Overflow](https://stackoverflow.com/).
- Additional self-lead projects and study on Python was found on [Codecademy](https://www.codecademy.com/learn) via the PRO subscription.
- Helpful Python videos on youtube by [Knowledge Mavens](https://www.youtube.com/c/KnowledgeMavens1).
- Helpful Python videos on youtube by [CS Students](https://www.youtube.com/channel/UCI1-IN8JwmFxtY_eVcIATTg).

### Technologies used
- Python
- Heroku.com
- GitHub
- GitPod

### Python Libraries used

- [Random](https://docs.python.org/3/library/random.html) - randint, .choice, randrange. were used to genreate random ship lengths, random directions and placements for ships, and by the RANDO cheat to determin a random location to target. 
- [Time](https://docs.python.org/3/library/time.html) - .sleep() was used in a variety of locations in the module, particularly to delay print messages and certain steps within methods. 
- [Snoop](https://pypi.org/project/snoop/) - The '@snoop' decorator was used extensively during testing when the script ran to large for a servie such as PythonTutor, snoop printed the code steps and return values of the relevant method to the terminal, allowing for me to debug issues deep into the games logic. 
- [PyFiglet](https://pypi.org/project/pyfiglet/0.7/) - Figlet was used to render some print text in the terminal through an illustrative font style, adding some visual elements to the text. 
- [OS](https://docs.python.org/3/library/os.html) - used to clear the terminal at various points within the game logic, in an IDE this will clear the terminal output, with heroku this will move the text currently printed in the terminal out of sight and above new text to be printed.
- [Itertools](https://docs.python.org/3/library/itertools.html) -.product was used to refactor a statement iterating through lists into a faster and more code effficient solution by locating the cartesian product of the given iterators.  

