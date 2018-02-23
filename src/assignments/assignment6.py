def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''

  
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0

    for ch in dna_string:
        if ch == 'A' or ch == 'a':
            count_A += 1
        elif ch == 'C' or ch == 'c':
            count_C += 1
        elif ch == 'G' or ch == 'g':
            count_G += 1
        elif ch == 'T' or ch == 't':
            count_T += 1

    return count_A,count_C,count_G,count_T
    print ('The letter A apears  ', count_A, 'times. ')
    print ('The letter C appears ', count_C, 'times. ')
    print ('The letter G appears ', count_G, 'times. ')
    print ('The letter T appears ', count_T, 'times. ')

