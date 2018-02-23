import unittest

from tests.assignments import test_assign6

suite = unittest.TestLoader().loadTestsFromModule(test_homework4)
unittest.TextTestRunner(verbosity=2).run(suite)
