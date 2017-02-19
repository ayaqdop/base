import unittest
import sys

sys.path.insert(0, "/home/ayaqdop/base")

from ioutils import IOUtils 

class IOTest(unittest.TestCase):

    def test_init(self):
        pass

    def test_is_valid_letter(self):
        target = IOUtils()
        self.assertTrue(target.is_valid_letter)
