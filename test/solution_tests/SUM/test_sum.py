from solutions.SUM import sum_solution


class TestSum():
    """Class to test sum_solution"""

    def test_sum(self):
        """Happy path test"""
        assert sum_solution.compute(1, 2) == 3

    # def test_sum(self):
    #     """Happy path test"""
    #     with self.assert_
    #     assert sum_solution.compute(1, 2) == 3

