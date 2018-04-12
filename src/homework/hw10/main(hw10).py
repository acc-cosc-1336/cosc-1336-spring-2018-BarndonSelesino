from src.homework.hw10.playerhw10 import Player
#write import statement for GameLog class
from src.homework.hw10.game_log import GameLog

#Create a game log instance
gl = GameLog()
#SEnd the game_log instance to Player class as an argument
Player(gl).roll_doubles()


#call the game log display method below
gl.display_log



