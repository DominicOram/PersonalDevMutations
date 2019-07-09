import unittest
from src.a_function import add_numbers_and_inc


class Tests(unittest.TestCase):
    def test_WHEN_numbers_added_THEN_return_greater_than_0(self):
        result = add_numbers_and_inc(3, 2)
        self.assertTrue(result > 0)

    def test_WHEN_numbers_added_THEN_return_int(self):
        result = add_numbers_and_inc(1, 2)
        self.assertTrue(type(result) == int)

    def test_WHEN_numbers_added_THEN_return_expected_value(self):
        result = add_numbers_and_inc(3, 2)
        self.assertEqual(result, 5)