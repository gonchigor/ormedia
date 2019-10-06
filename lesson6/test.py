# assert sum([1, 2, 2]) == 5, "should 5"
import unittest
from main import money, answer, recorder


class BotTest(unittest.TestCase):
    def test_money(self):
        self.assertEqual(money, 'BYN')

    def test_answer(self):
        self.assertIsInstance(answer, dict)

    def test_recorder(self):
        self.assertIsNone(recorder)

if __name__ == '__main__':
    unittest.main()
