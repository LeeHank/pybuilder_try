import unittest
from iqutils.data_preprocess import say_hi


class DataPreprocessTest(unittest.TestCase):
    def test_say_hi(self):
        res = say_hi()
        self.assertEqual(res, "Hi, there!")
