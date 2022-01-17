# test files should be named test_<description_of_what_testing>.py
import unittest
# inport function to test file
from evens import even_number_of_evens


# a test case which inherits from unittest.TestCase class
class TestEvens(unittest.TestCase):
    # # method name must begin with test_...
    # def test_function_returns_True(self):
    #     # use self to mean the current instance of the class
    #     self.assertTrue(even_number_of_evens([]))
    pass


if __name__ == "__main__":
    unittest.main()