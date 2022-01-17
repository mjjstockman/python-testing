# test files should be named test_<description_of_what_testing>.py
import unittest
# inport function to test file
from evens import even_number_of_evens


# a test case which inherits from unittest.TestCase class
class TestEvens(unittest.TestCase):

    def test_throws_error_if_value_passed_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)
    # # method name must begin with test_...
    # def test_function_returns_True(self):
    #     # use self to mean the current instance of the class
    #     self.assertTrue(even_number_of_evens([]))
    
    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)



if __name__ == "__main__":
    unittest.main()