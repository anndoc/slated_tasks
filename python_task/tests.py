import unittest

from question1 import main as main_question1
from question2 import main as main_question2


class TestQuestion1(unittest.TestCase):
    def test_question1(self):
        self.assertEqual(main_question1(2, 2), [[1, 2], [3, 4]])
        self.assertEqual(main_question1(2, 3), [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(main_question1(3, 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(main_question1(3, 4), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


class TestQuestion2(unittest.TestCase):
    def test_question2(self):
        self.assertEqual(main_question2('Abc@1,a B1#,2w3E*,2We#3345'), 'Abc@1,2w3E*')


if __name__ == "__main__":
    unittest.main()
