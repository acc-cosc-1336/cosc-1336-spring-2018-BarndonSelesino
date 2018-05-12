def convert_list_items_string_to_int(values):

    index = 0

    while index < len(values):

        values[index] = int(values[index])
        index += 1

    return values

file = None
file = open("survey.dat", "r")

for line in file:
    items = line.split()
    items = convert_list_items_string_to_int(items)
    display_histogram(items)
    
file.close()
