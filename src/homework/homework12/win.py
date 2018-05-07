from tkinter import Tk, Label, Button
from converter import Converter 
class Win(Tk):
    def __init__(self):

        Tk.__init__(self, None, None)
        self.display_labels = Button(self, text='Display Conv' ,command=self.display_labels).grid(row=3,column=0)
        self.quit_button = Button(self, text='quit', command =self.destroy).grid(row=3, column=1)
        self.mainloop()


    def display_labels(self):
    #fixed spelling on converter, please point it out to me if you see this
    #message
        self.converter = Converter()
        km = 100
        miles = self.converter.get_miles_from_km(km)
        self.labela = Label(self, text = 'km:' + str(km)) .grid(row=1)
        self.labelb = Label(self, text = 'miles:    ' + format(miles, '.2f')).grid(row=2)
        self.mainloop()
