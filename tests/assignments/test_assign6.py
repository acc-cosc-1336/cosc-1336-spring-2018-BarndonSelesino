import unittest
#write the import for function get_count_A_C_G_and_T_in_string
from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string

class Test_Assign6(unittest.TestCase):

    def test_countACGT_w_string_ATGCTTCAGAAAGGTCTTACG(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string ATGCTTCAGAAAGGTCTTACG
        '''
        valcount_A,valcount_C,valcount_G,valcount_T = get_count_A_C_G_and_T_in_string('ATGCTTCAGAAAGGTCTTACG')
        self.assertEqual(6,valcount_A)
        self.assertEqual(4,valcount_C)
        self.assertEqual(5,valcount_G)
        self.assertEqual(6,valcount_T)
        

    def test_count_ACGT_w_stringAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string
        AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
        '''
        valcount_A,valcount_C,valcount_G,valcount_T = get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
        self.assertEqual(20, valcount_A)
        self.assertEqual(12, valcount_C)
        self.assertEqual(17, valcount_G)
        self.assertEqual(21, valcount_T)



unittest.main(verbosity=2)
