#write import statement for ScoreEntry
from score_entry import ScoreEntry
#1create a class named GameLog with a parameterless constructor-create an empty list of score_entries class attribute in
# constructor
#2Create a class method add_score_entry with a score_entry parameter, in the method code append the score_entry parameter
#to the score_entries class attribute
#3Create a display_log method with no parameters-in this method iterate through display_log and display each
#score entry to screen
#1
class GameLog():
    def __init__(self):
        self.score_enteries = []

#2
    def add_score_entry(self,score_entry):
        self.score_enteries.append(score_entry)
#3
    def display_log(self):
        if i in self.score_enteries:
            print('Portfolio:    ', value.score_entry_id, 'r1:', die1_value, 'r2:', die2_value)
        else:
            print('No Data')
