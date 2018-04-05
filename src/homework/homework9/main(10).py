#write import statements for Player and Die class
from die import Die
from player import Player

#Create an instance of the Main class and call/execute the roll_doubles method

class Main():

    def game_test(self):
        self.player = Player()
        self.player.roll_doubles()
main = Main()
main.game_test()
