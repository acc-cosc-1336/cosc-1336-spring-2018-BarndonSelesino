
#write the import statements for homework5 functions

#With the functions created in homework5...
#Prompt user for number of sales records to input.
#Open a file for text writing.
#Iterate and prompt user for item name and price.
#Save item name and price to file in one line
#Calculate sum of price and write to file
#Calculate average price and write to file

#Open a file for text reading.
#Read the saved file and output table

from homework5 import (write_sales_data, read_sales_data)


def main():
#defining sales_record
    infile = open('sales_records.txt', 'w')
    infile.write('name' + '\t' + 'price' + '\n')
    num_of_items = int(input("Enter number of items: "))

#defining price, itemnames
    tnoi = 0
    for items in range(1, num_of_items+1):
        item = input('Enter name of item: ')
        price = float(input('Enter price of item: '))
        infile.write(str(item)+ '\t')
        infile.write(str("{0:.2f}".format(price))+ '\n')
        tnoi += price
#definingtotal
    infile.write('total' + '\t'+ str("{0:.2f}".format(tnoi))+ '\n')
    avg = tnoi / num_of_items
    infile.write('Avg' + '\t'+ str("{0:.2f}".format(avg)))
    infile.close()
#readingeverything        
    infile = open('sales_records.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)
        
main()

