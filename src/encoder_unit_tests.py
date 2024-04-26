import unittest
from pylogic import *

class TestEncoder(unittest.TestCase):
    def test_encoder_1_bit(self):
        encoder = Encoder(input_size=1)

        # Test input 0
        encoder[0].set_value(1)
        encoder.update()
        self.assertEqual(encoder["out"].get_value(), 0)

        # Test input 1
        encoder[0].set_value(0)
        encoder.update()
        self.assertEqual(encoder["out"].get_value(), 1)

    def test_encoder_2_bit(self):
        encoder = Encoder(input_size=2)

        # Test input 00
        encoder[0].set_value(1)
        encoder[1].set_value(1)
        encoder.update()
        self.assertEqual(encoder["out"].get_value(), 0)

        # Test input 01
        encoder[0].set_value(0)
        encoder[1].set_value(1)
        encoder.update()
        self.assertEqual(encoder["out"].get_value(), 1)

        # Test input 10
        encoder[0].set_value(1)
        encoder[1].set_value(0)
        encoder.update()
        self.assertEqual(encoder["out"].get_value(), 2)

        # Test input 11
        encoder[0].set_value(0)
        encoder[1].set_value(0)
        encoder.update()
        self.assertEqual(encoder["out"].get_value(), 3)

if __name__ == "__main__":
    unittest.main()

# THIS TEST DOES NOT WORK WITH THE PYLOGIC LIBRARY, PLEASE SEEN INDIVIDUAL COMPONENT DEMOS IN ORDER TO SEE THE FUNCTION OF THE CODE
# SEPARATED FROM THE PYLOGIC LIBRARY. THESE DEMOS ARE PURELY TO DEMONSTRATE THAT THE ESSENCE OF THE COMPONENT ADDITIONS WORK, BUT
# THEY EXPERIENCE ISSUES DUE TO THE FUNDAMENTALS OF THE PYLOGIC LIBRARY