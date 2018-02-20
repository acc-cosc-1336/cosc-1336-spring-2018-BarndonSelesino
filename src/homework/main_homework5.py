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

#defining sales records
def main():
    salesrecords = ['price', 'itemname']

#defining amount of sales

    num_of_sales = int(input("Please enter the amount of total sales:    "))


#defining sum and avg
    sum_of_price = sum(price)

    for num_of_sales in range(1, num_of_sales +1):
        avg_price = sum_of_price / num_of_sales
#opening file for writing
    outfile = open('salesrecords.txt' , 'w')
#defining item name and price
    for item in salesrecords:
        outfile.write(item + '\n')
    for price in salesrecords:
        outfile.write(price + '\n')
    outfile.writeline(item, price)

#sum of price
    
    for sum_of_price in salesrecords:
        outfile.write(sum_of_price + '\n')
    outfile.writeline(sum_of_price)

#avg of price
    for avg_price in salesrecords:
        outfile.write(avg_price + '\n')
    outfile.writeline(avg_price)

#Reading a file now
    infile = open('salesrecords.txt' , 'r')
#closing file
    infile.close()
#stripping /n
    index = 0
    while index < len(salesrecords):
        salesrecords[index] = salesrecords[index].rstrip('\n')
        index += 1
#printing the program
    print(salesrecords)
main()
    
    
