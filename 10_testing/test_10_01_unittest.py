import unittest
import math


def root_multiply(num1, num2):
    """Function to calculate the squared root of num1 and multiply it by num2"""
    if num1 < 0:
        raise ValueError("Please don't use a negative value")
    rt = math.sqrt(num1)
    return rt * num2

class TestExercise1(unittest.TestCase):
    """Class to test 10_01_unittest"""
    def test_root_multiply_with_normal_numbers(self):
        self.assertEqual(root_multiply(16,2), 8)
        self.assertEqual(root_multiply(16, -2), -8)
        self.assertEqual(root_multiply(0, 2), 0)
        self.assertEqual(root_multiply(4, 2.5), 5)
        self.assertEqual(root_multiply(2, 2), 2.8284271247461903)
        self.assertEqual(root_multiply(16, 0), 0)
        with self.assertRaises(ValueError):
            root_multiply(-1, 2)
        self.assertEqual(root_multiply(1, math.pi), 2*math.pi)
        # Last one is wrong on purpose


if __name__ == '__main__':
    unittest.main()
