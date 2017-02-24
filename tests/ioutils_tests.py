import unittest
import sys

sys.path.insert(0, "/home/ayaqdop/base")

from ioutils import IOUtils 

class IOTest(unittest.TestCase):

    def test_init(self):
        pass

    def test_is_valid_letter_true(self):
        target = IOUtils()
        self.assertTrue(target.is_valid_letter('a'))
        self.assertTrue(target.is_valid_letter('A'))

    def test_is_valid_letter_false(self):
        target = IOUtils()
        self.assertFalse(target.is_valid_letter('w'))
        self.assertFalse(target.is_valid_letter('W'))

    def test_is_not_same_pos_true(self):
        target = IOUtils()
        self.assertTrue(target.is_not_same_pos(23,25))

    def test_is_not_same_pos_false(self):
        target = IOUtils()
        self.assertFalse(target.is_not_same_pos(23,23))




























































