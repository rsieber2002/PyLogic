import unittest
from pylogic import *

class TestDecoder(unittest.TestCase):
    def test_decoder_1_bit(self):
        decoder = Decoder(input_size=1)
        decoder["in"].set_value(0)
        decoder.update()
        self.assertEqual(decoder[0].get_value(), 1)
        self.assertEqual(decoder[1].get_value(), 0)

        decoder["in"].set_value(1)
        decoder.update()
        self.assertEqual(decoder[0].get_value(), 0)
        self.assertEqual(decoder[1].get_value(), 1)

    def test_decoder_2_bit(self):
        decoder = Decoder(input_size=2)

        # Test input 00
        decoder["in"].set_value(0)
        decoder.update()
        self.assertEqual(decoder[0].get_value(), 1)
        self.assertEqual(decoder[1].get_value(), 0)
        self.assertEqual(decoder[2].get_value(), 0)
        self.assertEqual(decoder[3].get_value(), 0)

        # Test input 01
        decoder["in"].set_value(1)
        decoder.update()
        self.assertEqual(decoder[0].get_value(), 0)
        self.assertEqual(decoder[1].get_value(), 1)
        self.assertEqual(decoder[2].get_value(), 0)
        self.assertEqual(decoder[3].get_value(), 0)

        # Test input 10
        decoder["in"].set_value(2)
        decoder.update()
        self.assertEqual(decoder[0].get_value(), 0)
        self.assertEqual(decoder[1].get_value(), 0)
        self.assertEqual(decoder[2].get_value(), 1)
        self.assertEqual(decoder[3].get_value(), 0)

        # Test input 11
        decoder["in"].set_value(3)
        decoder.update()
        self.assertEqual(decoder[0].get_value(), 0)
        self.assertEqual(decoder[1].get_value(), 0)
        self.assertEqual(decoder[2].get_value(), 0)
        self.assertEqual(decoder[3].get_value(), 1)

if __name__ == "__main__":
    unittest.main()

# THIS TEST DOES NOT WORK WITH THE PYLOGIC LIBRARY, PLEASE SEEN INDIVIDUAL COMPONENT DEMOS IN ORDER TO SEE THE FUNCTION OF THE CODE
# SEPARATED FROM THE PYLOGIC LIBRARY. THESE DEMOS ARE PURELY TO DEMONSTRATE THAT THE ESSENCE OF THE COMPONENT ADDITIONS WORK, BUT
# THEY EXPERIENCE ISSUES DUE TO THE FUNDAMENTALS OF THE PYLOGIC LIBRARY