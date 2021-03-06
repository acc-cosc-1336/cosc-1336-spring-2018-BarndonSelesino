import unittest

#write import statement for homework 7 file
from homework7 import get_pdist, get_p_distance_matrix

class TestHomework7(unittest.TestCase):
    def test_p_distance(self):
        self.assertEqual(.4, get_pdist(( ['T','T','T','C','C','A','T','T','T','A'],\
             ['G','A','T','T','C','A','T','T','T','C']))) 

    def test_get_p_distance_matrix(self):
        dna = [['T','T','T','C','C','A','T','T','T','A'],\
             ['G','A','T','T','C','A','T','T','T','C'],\
             ['T','T','T','C','C','A','T','T','T','T'],\
             ['G','T','T','C','C','A','T','T','T','A']]
        pdist = [[0.00000, 0.40000, 0.10000, 0.10000]\
                 [0.40000,0.0000,0.40000,0.30000]\
                 [0.10000,0.40000, 0.00000, 0.20000]\
                 [0.10000, 0.30000, 0.20000, 0.00000]]




    def test_sample(self):
        self.assertEqual(1,1)

    #create a test for get p distance matrix with following data
    '''
    Sample Dataset
    [
     ['T','T','T','C','C','A','T','T','T','A'],
     ['G','A','T','T','C','A','T','T','T','C'],
     ['T','T','T','C','C','A','T','T','T','T'],
     ['G','T','T','C','C','A','T','T','T','A']
    ]
    
    Sample Output
    0.00000 0.40000 0.10000 0.10000
    0.40000 0.00000 0.40000 0.30000
    0.10000 0.40000 0.00000 0.20000
    0.10000 0.30000 0.20000 0.00000

    '''

    
