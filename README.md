# Tower Defense Game - PyGame and PyQt6

## Project Information
 - Creator: Axel Hedman
 - Programming Language: Python 3
 - Libraries: PyGame, PyQt

## Introduction
In this repository you will find two different tower defense games, one developed with PyGame and one developed with PyQt6. I developed these programs as a final project for a Python course at Aalto University. Below you will find a short description of the programs and instructions on how to run them on your computer.

## PyGame

The PyGame version includes three main states that the player will encounter: a main menu, a level editor, and a game window. Below is a short description of the three different states.

#### Main Menu
When running the program the player is greeted by the main menu. The main purpose of this state is to help the player navigate between the level editor and the game window. 

![Main Menu](\assets\main_menu.png)

#### Level Editor
Here the player is able to create a custom map to play on. The 12X8 map grid is made up of tiles. In the level editor every tile has four modes: road, grass, start, and finnish. To draw a map the player can simply click the different tiles to switch between these four modes. Every map has to start and end at the edge of the grid. Remember to set a start and a end tile before saving the map. If the map is unreadable, a default map will be set.

![Level Editor](\assets\level_editor.png)

#### Game Window
The game window consists of a map and a menu containing towers. In the menu, the lives and money of the player is also displayed. Towers can be bought and placed to stop the enemies from reaching the base. More money can be generated by killing enemies and clearing waves. The player starts the game with 3 lives. If an enemy reaches the base, one life is lost. At 0 lives, the game is lost.

There are three different types of towers: basic tower, ice tower, and poison tower. The basic tower shoots a projectile that damages a single enemy. The ice tower shoots a projectile that freezes an enemy for a short period of time without damaging it. The poison tower shoots a projectile that poisons enemies. Poisoned enemies take damage over time (note: freeze and poison effects doesn't stack). Towers can be sold for 50% of their initial price. To win the game, the player has to survive 5 waves of enemies. The different types of enemies are: basic enemy, stealth enemy, and boss enemy. The basic enemy is affected all towers, the stealth enemy is immune to poison, and the boss enemy can't be frozen. When killed, the boss enemy will spawn 3 basic enemies that continues where the boss enemy died. 

![Game Window](\assets\game.png)

## PyQt6
The PyQt6 program is a bit simpler than the PyGame program. I mainly developed it for comparison between the libraries. The PyQt6 game only consists of one state. When you run the program you are greeted by the game window. Play the game by placing a tower and clicking the "next wave button".

![PyQt game](\assets\pyqt.png)

## Running the Programs
Before running these programs, make sure that python 3 is installed on your computer. PyGame and PyQt6 are installed using pip, which is the package installer for Python. To install pip on Linux, run the following command in the terminal: 
```
sudo apt install python3-pip
```
To install pip on Windows, follow this tutorial: https://www.dataquest.io/blog/install-pip-windows/

With pip installed we can now install PyGame and PyQt by executing the following command in the terminal:
```
pip install pygame, pyqt6
```
This command works for both Linux and Windows.

To run the different programs, navigate to the project root directory in the terminal and execute:

1. PyGame
```python3 PyGame_src/main.py``` on Linux, or:
``` python PyGame_src/main.py ``` on Windows.

2. PyQt6
```python3 PyQt_src/main.py``` on Linux, or:
```python PyQt_src/main.py``` on Windows.

Have fun playing :D