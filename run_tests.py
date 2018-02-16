import unittest

from tests.assigments import test_assign5

suite = unittest.TestLoader().loadTestsFromModule(test_assign5)
unittest.TextTestRunner(verbosity=2).run(suite)
