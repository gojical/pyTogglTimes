import unittest
from tools import get_config


class TestConfig(unittest.TestCase):
    def readConfig(self):
        # create mock file

        config = get_config()
        # self.assertEqual(fun(3), 4)
