import unittest

class Subtractor:
    def __init__(self, input_bits):
        self.input_bits = input_bits
        self.output_bits = [0] * len(input_bits)

    def subtract(self, operand):
        if len(operand) != len(self.input_bits):
            raise ValueError("Operand length does not match input bits")
        
        borrow = 0
        for i in range(len(self.input_bits)):
            diff = self.input_bits[i] - operand[i] - borrow
            self.output_bits[i] = diff % 2
            borrow = 1 if diff < 0 else 0

    def get_output(self):
        return self.output_bits

class TestSubtractor(unittest.TestCase):
    def test_subtraction(self):
        input_bits = [1, 0, 1, 0]  # Represents 10 in binary
        operand = [0, 1, 0, 1]     # Represents 5 in binary
        expected_output = [1, 1, 0, 1]  # Represents 5 in binary
        subtractor = Subtractor(input_bits)
        subtractor.subtract(operand)
        self.assertEqual(subtractor.get_output(), expected_output)

    def test_subtraction_with_borrow(self):
        input_bits = [1, 0, 1, 0]  # Represents 10 in binary
        operand = [1, 0, 1, 1]     # Represents 13 in binary
        expected_output = [1, 1, 1, 1]  # Represents -3 in binary (with borrow)
        subtractor = Subtractor(input_bits)
        subtractor.subtract(operand)
        self.assertEqual(subtractor.get_output(), expected_output)

    def test_invalid_operand_length(self):
        input_bits = [1, 0, 1, 0]  # Represents 10 in binary
        operand = [1, 0, 1]        # Invalid length
        subtractor = Subtractor(input_bits)
        with self.assertRaises(ValueError):
            subtractor.subtract(operand)

if __name__ == '__main__':
    unittest.main()


