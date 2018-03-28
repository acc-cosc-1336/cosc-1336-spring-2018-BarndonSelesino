from homework8 import add_inventory, remove_inventory_widget
import pickle
'''
Write a main function to create an empty dictionary and
a user-controlled loop to prompt for a widget name and quantity.
Add the values to the dictionary as key(widget name) and value(quantity) pairs.

After user decides to exit write data to file .

'''
def main():
    widgets = {}
    data = 'y'
    while data.lower() == 'y' or data.lower() == 'Y':
        widget_name = input('Enter a name:  ')
        quantity = int(input('enter a numeric value:   '))
        widget_names_and_quantity = add_inventory(widget_name, quantity, widgets)
        data = input('Continue Y/N?:      ')
    else:
        
        file_object = open('widgets_dictionary.dat', 'wb')
        pickle.dump(widgets, file_object)
        file_object.close()
       
main()
        
    

