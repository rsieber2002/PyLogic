import unittest
from pylogic import *

class TestEncoder(unittest.TestCase):
    def test_encoder_output(self):
        # Test a 3-to-2 encoder
        encoder = Encoder(3)

        # Set the first input line (index 0) to active (1)
        encoder[0].set_value(1)
        self.assertEqual(encoder["out"].get_value(), 0b00)

        # Set the second input line (index 1) to active (1)
        encoder[1].set_value(1)
        self.assertEqual(encoder["out"].get_value(), 0b01)

        # Set the third input line (index 2) to active (1)
        encoder[2].set_value(1)
        self.assertEqual(encoder["out"].get_value(), 0b10)

    def test_encoder_no_input(self):
        # Test when no input line is active
        encoder = Encoder(4)
        self.assertIsNone(encoder["out"].get_value())

    def test_encoder_invalid_input(self):
        # Test invalid input (outside the range)
        encoder = Encoder(2)
        encoder[3].set_value(1)  # This input line is outside the range [0, 1]
        self.assertIsNone(encoder["out"].get_value())

if __name__ == "__main__":
    unittest.main()
