from solutions.HLO import hello_solution


class TestHello():
    """Class to test sum_solution"""

    def test_hello_world(self):
        """Happy path test"""
        assert hello_solution.hello("") == "Hello, world!"
