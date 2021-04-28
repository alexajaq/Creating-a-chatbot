import unittest
from unittest.mock import patch

# from sum import sum

import nameasker


class TestListSum(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'test_bot',

    ])
    def test_sum_string_of_ints(self, mock_inputs):
        result = nameasker
        print(result)
        self.assertEqual(result, 15)

    # @patch('builtins.input', side_effect=[10, string_of_ints_2])
    # def test_sum_string_of_ints_2self, mock_inputs):
    #     result=sum()
    #     self.assertEqual(result, 10)
