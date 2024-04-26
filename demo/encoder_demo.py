import unittest

class Encoder:
    def __init__(self, input_size):
        self.input_size = input_size

    def encode(self, input_bits):
        if len(input_bits) != self.input_size:
            raise ValueError("Input size mismatch")

        encoded_value = 0
        for i in range(self.input_size):
            bit = input_bits[i]
            if bit not in (0, 1):
                raise ValueError("Input bit must be 0 or 1")
            encoded_value |= (bit << i)

        return encoded_value

class TestEncoder(unittest.TestCase):
    def test_encoder_1_bit(self):
        encoder = Encoder(input_size=1)

        # Test input 0
        encoded_value = encoder.encode([1])
        self.assertEqual(encoded_value, 0)

        # Test input 1
        encoded_value = encoder.encode([0])
        self.assertEqual(encoded_value, 1)

    def test_encoder_2_bit(self):
        encoder = Encoder(input_size=2)

        # Test input 00
        encoded_value = encoder.encode([1, 1])
        self.assertEqual(encoded_value, 0)

        # Test input 01
        encoded_value = encoder.encode([0, 1])
        self.assertEqual(encoded_value, 1)

        # Test input 10
        encoded_value = encoder.encode([1, 0])
        self.assertEqual(encoded_value, 2)

        # Test input 11
        encoded_value = encoder.encode([0, 0])
        self.assertEqual(encoded_value, 3)

    def test_encoder_invalid_input_size(self):
        encoder = Encoder(input_size=3)

        with self.assertRaises(ValueError):
            encoded_value = encoder.encode([0, 1])  # Input size mismatch

    def test_encoder_invalid_input_bits(self):
        encoder = Encoder(input_size=2)

        with self.assertRaises(ValueError):
            encoded_value = encoder.encode([2, 1])  # Invalid input bit

if __name__ == "__main__":
    unittest.main()
    