import unittest
from prime_generator import prime_number_generator


class PrimeGeneratorTestCases(unittest.TestCase):
    def test_generator_returns_correct_result(self):
        result = prime_number_generator(10)
        self.assertEqual([2, 3, 5, 7], result)

    def test_generator_returns_list(self):
        result = prime_number_generator(12)
        self.assertEqual(type(result), list, msg='Invalid output')

    def test_generator_raises_exception_for_non_integer_args(self):
        with self.assertRaises(TypeError) as context:
            prime_number_generator('ten')
            self.assertEqual(
                "Argument must be an integer",
                context.exception.message, "Invalid input"
            )

    def test_generator_returns_list_of_integers(self):
        result = prime_number_generator(15)
        self.assertTrue(all(isinstance(n, int) for n in result), msg="Generator returns list with non-integer items")

    def test_generator_returns_empty_list_for_negative_values(self):
        result = prime_number_generator(-10)
        self.assertEqual(result, [], msg='Function should return empty list for negative arguments')

if __name__ == '__main__':
    unittest.main()