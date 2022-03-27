import unittest

from solutions.SUM import sum_solution


class TestSum(unittest.TestCase):
    """Class to test sum_solution"""

    def test_sum(self):
        """Happy path test"""
        assert sum_solution.compute(1, 2) == 3

    # def test_check_bounds(self):
    #     """Raise value error if integer passed in is out of limit"""
    #     with self.assertRaises
    #     assert sum_solution.compute(1, 2) == 3



