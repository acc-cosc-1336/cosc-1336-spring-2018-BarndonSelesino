import unittest

#write import statement for homework 7 file


class TestHomework7(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1,1)

    #create a test for get p distance matrix with following data
    def test_get_p_distance_matrix(self):
        self.assertEqual([[0, 0.40, 0.10, 0.10], [0.40, 0, 0.40, 0.30], [0.10, 0.40, 0, 0.20], [0.10, 0.30, 0.20, 0]],get_p_distance_matrix([
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]))
    
    
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

    
