import unittest
from tools import get_config


class TestConfig(unittest.TestCase):
    def read_config(self):
        # create mock file

        config = get_config()
        self.assertEqual(2, 1)
        # self.assertEqual(fun(3), 4)
