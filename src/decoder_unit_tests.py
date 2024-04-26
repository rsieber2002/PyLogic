import unittest
from pylogic import *

class TestDecoder(unittest.TestCase):
    def test_decoder_output(self):
        # Test a 2-to-4 decoder
        decoder = Decoder(4)
        decoder["in"].set_value(0)
        output_values = [decoder[i].get_value() for i in range(4)]
        self.assertEqual(output_values, [1, None, None, None])

        decoder["in"].set_value(3)
        output_values = [decoder[i].get_value() for i in range(4)]
        self.assertEqual(output_values, [None, None, None, 1])

        decoder["in"].set_value(1)
        output_values = [decoder[i].get_value() for i in range(4)]
        self.assertEqual(output_values, [None, 1, None, None])

    def test_decoder_invalid_input(self):
        # Test invalid input (outside the range)
        decoder = Decoder(3)
        decoder["in"].set_value(5)  # This input value is outside the range [0, 2]
        output_values = [decoder[i].get_value() for i in range(3)]
        self.assertEqual(output_values, [None, None, None])  # All outputs should be zero

if __name__ == "__main__":
    unittest.main()
