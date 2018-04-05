#write import statement for Die class
from die import Die
'''
Create a Player class.

'''

class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''
        self.die1 = Die()
        self.die2 = Die()

    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        dice1 = 1
        dice2 = 2
        while dice1 != dice2:
            dice1 = self.die1.roll()
            print('The roll of dice 1 is:    ', dice1)
            dice2 = self.die2.roll()
            print('The roll of dice 2 is:    ', dice2)
        else:
            print('You have rolled doubles and both dice have die(d)')


