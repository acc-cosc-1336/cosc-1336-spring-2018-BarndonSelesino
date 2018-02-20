#Create a function named write_sales_data with file_object, item and price as parameters.
#The function should write item and price to a file.

#Create another function named read_sales_data with file_object as a parameter.
#The function will read the file line by line and display to screen to produce the table described in homework 5.
def write_sales_data(file_object,item,price)
    file_object = ['']
        outfile = open('salesrecords.txt', 'w')
        for file_object in salesrecords:
            outfile.write(file_object + '\n')
        outfile.close()
# item and price
    item = ['']
        outfile = open('salesrecords.txt', 'w')
        for item in salesrecords:
            outfile.write(items + '\n')
        outfile.close()
    price = ['']
        outfile = open('salesrecords.txt', 'w')
        for price in salesrecords:
            outfile.write(price + '\n')
        outfile.close()
write_sales_data()

def read_sales_data(file_object)    
    infile = open('salesrecords.txt', r)
    file_object
