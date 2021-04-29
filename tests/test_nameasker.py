from typing import Any, Dict, List
import unittest
from unittest.mock import patch
from src.nameasker import give_user_the_third_degree


class TestNameAsker(unittest.TestCase):
    int
    """[summary] Patches keyboard input to automatically interact with the program under test
    """

# TODO: use MagicMock
    def test_do_the_stuff(self):
        """
        This test calls the function under test, give_user_the_third_degree.        """

        # arrange
        # we define our own typed responses and send them to input() in order
        inputs: List[str] = [
            'test_bot',
            'likewise',
            'bits and bytes every morning',
            'y'
        ]

        # the activity summary returned by the function
        expected_result: Dict[str, Any] = {
            'name': inputs[0],
            'food': inputs[2],
            'story_told': True
        }

        # act
        with patch('builtins.input', side_effect=inputs):
            result: Dict[str, Any] = give_user_the_third_degree()

        # assert
        # here we compare the returned value with what we expected
        print(result)
        self.assertDictEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
