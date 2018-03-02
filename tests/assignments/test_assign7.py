import unittest
#write the import for function for assignment7 sum_list_values
from assignment7 import sum_list_values

class Test_Assign7(unittest.TestCase):

    def sample_test(self):
        self.assertEqual(1,1)

    #create a test for the sum_list_values function with list elements:
    # bill 23 16 19 22

    def sum_list_values(self):
        self.assertEqual('bill', 23, 16, 19, 22)
