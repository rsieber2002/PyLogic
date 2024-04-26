import unittest

class Decoder:
    def __init__(self, input_size):
        self.input_size = input_size
        self.num_outputs = 2 ** input_size

    def decode(self, input_value):
        if not 0 <= input_value < self.num_outputs:
            raise ValueError("Input value out of range")

        output_bits = []
        for i in range(self.input_size):
            bit = (input_value >> i) & 1
            output_bits.append(bit)

        return output_bits

class TestDecoder(unittest.TestCase):
    def test_decoder_1_bit(self):
        decoder = Decoder(input_size=1)

        # Test input 0
        output_bits = decoder.decode(0)
        self.assertEqual(output_bits, [0])

        # Test input 1
        output_bits = decoder.decode(1)
        self.assertEqual(output_bits, [1])

    def test_decoder_2_bit(self):
        decoder = Decoder(input_size=2)

        # Test input 00
        output_bits = decoder.decode(0)
        self.assertEqual(output_bits, [0, 0])

        # Test input 01
        output_bits = decoder.decode(1)
        self.assertEqual(output_bits, [1, 0])

        # Test input 10
        output_bits = decoder.decode(2)
        self.assertEqual(output_bits, [0, 1])

        # Test input 11
        output_bits = decoder.decode(3)
        self.assertEqual(output_bits, [1, 1])

    def test_decoder_invalid_input_value(self):
        decoder = Decoder(input_size=2)

        with self.assertRaises(ValueError):
            output_bits = decoder.decode(4)  # Input value out of range

if __name__ == "__main__":
    unittest.main()
