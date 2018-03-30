import unittest

from tests.assignments import assign9

suite = unittest.TestLoader().loadTestsFromModule(test_assign9)
unittest.TextTestRunner(verbosity=2).run(suite)
