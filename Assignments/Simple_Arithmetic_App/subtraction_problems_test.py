import unittest

import subtraction_problems

class Test_subtraction_problems_function(unittest.TestCase):

#    def test_the_function_doesnt_collects_argument(self):
#        actual = subtraction_problems.random_subtraction(9)
#        expected = "random_subtraction() takes 0 positional arguments but 1 was given"
#        self.assertEqual(actual,expected)


    def test_the_function_returns_the_correct_message_if_you_passed(self):
        actual = subtraction_problems.random_subtraction(9)
        expected = "random_subtraction() takes 0 positional arguments but 1 was given"
        self.assertEqual(actual,expected)
