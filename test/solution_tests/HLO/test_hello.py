from solutions.HLO import hello_solution


class TestHello():
    """Class to test sum_solution"""

    def test_hello(self):
        """Happy path test"""
        friend = "John"
        assert hello_solution.hello(friend) == f"Hello, {friend}!"
