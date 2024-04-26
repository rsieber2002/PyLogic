import unittest
from pylogic import *

class TestSubtractor(unittest.TestCase):
    def test_subtractor_output(self):
        # Test case: 5 - 3 = 2
        subtractor = Subtractor(4)
        subtractor["A"].set_value(5)
        subtractor["B"].set_value(3)
        subtractor["Bi"].set_value(0)  # Borrow in is 0
        subtractor.update()
        self.assertEqual(subtractor["D"].get_value(), 2)
        self.assertEqual(subtractor["Bo"].get_value(), 0)  # No borrow out

        # Test case: 3 - 5 = -2 (represented as 14 in 4-bit 2's complement)
        subtractor["A"].set_value(3)
        subtractor["B"].set_value(5)
        subtractor["Bi"].set_value(1)  # Borrow in is 1
        subtractor.update()
        self.assertEqual(subtractor["D"].get_value(), 14)
        self.assertEqual(subtractor["Bo"].get_value(), 1)  # Borrow out is 1

        # Test case: 7 - 7 = 0
        subtractor["A"].set_value(7)
        subtractor["B"].set_value(7)
        subtractor["Bi"].set_value(0)  # Borrow in is 0
        subtractor.update()
        self.assertEqual(subtractor["D"].get_value(), 0)
        self.assertEqual(subtractor["Bo"].get_value(), 0)  # No borrow out

    def test_subtractor_invalid_input(self):
        # Test case: One of the inputs is None
        subtractor = Subtractor(4)
        subtractor["A"].set_value(5)
        subtractor["Bi"].set_value(0)  # Borrow in is 0
        subtractor.update()
        self.assertIsNone(subtractor["D"].get_value())
        self.assertIsNone(subtractor["Bo"].get_value())

if __name__ == "__main__":
    unittest.main()

# THIS TEST DOES NOT WORK WITH THE PYLOGIC LIBRARY, PLEASE SEEN INDIVIDUAL COMPONENT DEMOS IN ORDER TO SEE THE FUNCTION OF THE CODE
# SEPARATED FROM THE PYLOGIC LIBRARY. THESE DEMOS ARE PURELY TO DEMONSTRATE THAT THE ESSENCE OF THE COMPONENT ADDITIONS WORK, BUT
# THEY EXPERIENCE ISSUES DUE TO THE FUNDAMENTALS OF THE PYLOGIC LIBRARY