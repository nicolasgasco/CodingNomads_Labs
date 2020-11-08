'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''
import unittest

class TestDivideFunction(unittest.TestCase):
    """Class to test a simple functions to dive two numbers"""

    def test_division_function(self):
        self.assertEqual(division(16, 2), 8)
        self.assertEqual(division(16, -2), -8)
        self.assertEqual(divsion(0, 2), 0)
        self.assertEqual(division(16, 0), 0)
        self.assertEqual(division(-1, 10), -0,1)
        self.assertEqual(division(1, math.pi), 0.3183098861837907)

# Function to read and write to file
class TestWritingFunc(unittest.TestCase):
    """Class to test a funcion which opens and writes a text"""
    def test_open_write_close(self):
        self.assertEqual(".txt", "test_file.txt"[-4:])
        self.assertEqual(".txt", "test_file"[-4:])
        with self.assertRaises(FileNotFoundError):
            open_write_close("inexistentfile.txt", "Please write this")
        with self.assertRaises(NameError):
            open_write_close("inexistentfile.txt", open)


if __name__ == '__main__':
    unittest.main()



