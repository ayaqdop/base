import unittest
import sys
import string

sys.path.insert(0, "/home/ayaqdop/base")

from ioutils import IOUtils 

class IOTest(unittest.TestCase):

    def test_init(self):
        pass

    def test_is_valid_letter_single_letters(self):
        target = IOUtils()

        for c in string.ascii_lowercase:
            if c < 'q':
                self.assertTrue(target.is_valid_letter(c))
            else:
                self.assertFalse(target.is_valid_letter(c))

        for c in string.ascii_uppercase:
            if c < 'Q':
                self.assertTrue(target.is_valid_letter(c))
            else:
                self.assertFalse(target.is_valid_letter(c))

    def test_is_valid_letter_false(self):
        target = IOUtils()
        self.assertFalse(target.is_valid_letter("False"))
        self.assertFalse(target.is_valid_letter("false"))
       
    def test_is_not_same_position_true(self):
        target = IOUtils()
        self.assertTrue(target.is_not_same_position(23,25))

    def test_is_not_same_position_false(self):
        target = IOUtils()
        self.assertFalse(target.is_not_same_position(23,23))

    def test_is_valid_number_false(self):
        target = IOUtils()
        self.assertFalse(target.is_valid_number("42"))
        self.assertFalse(target.is_valid_number(0))
        self.assertFalse(target.is_valid_number(25))
        self.assertFalse(target.is_valid_number(-7))
