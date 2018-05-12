class SalariedEmployee:
    def __init__(self,yearly_rate):
        self.yearly_rate = yearly_rate

    def calculate_bw_rate(self):
        return yearly_rate / 26
        #52 weeks in a year, biweekly makes 26 weeks
