'''
Create a function sum_list_values that takes a list parameter and returns the sum of all the numeric values in the list.

Sample Data
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89
'''
#joe_list = [10, 15, 20, 30, 40]
#bill_list = [23, 16, 19, 22]
#sue_list = [8, 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17]
#grace_list = [12, 28, 21, 45, 26, 10]
#john_list = [14, 32, 25, 16, 89]
#total = 0

def sum_list_values(value_list):
    total = 0
    index = 1
    while index < len (value_list):
        total += value_list[index]
    return(total)
  




#sum_list_values(list)
#print(sum(num))
#total = 0
    #for value in (joe_list, bill_list, sue_list, grace_list, john_list):
        #total += value
    #print(total)



