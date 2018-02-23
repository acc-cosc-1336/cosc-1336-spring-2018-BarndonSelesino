#write the import for the function get_count_A_C_G_and_T_in_string from assignment 6 file

'''
Using function get_count_A_C_G_and_T_in_string create a main function and...
Call the function get_count_A_C_G_and_T_in_string from assignment 6 file
With the string AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC as an argument
Sample Output:

DNA String:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
A 20, C 12, G 17, T 21


Call the main function in Python Shell or in this file.
'''
from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string
def main():
    valcount_A,valcount_C,valcount_G,valcount_T = get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    print('DNA string')
    print('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    print('A ', str(valcount_A),'  C  ', str(valcount_C), '  G  ' , str(valcount_G), '  T  ', str(valcount_T))
   


main()
