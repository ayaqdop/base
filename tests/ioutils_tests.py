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

    def test_is_valid_position(self):
        target = IOUtils()
        self.assertTrue(target.is_valid_position("a0"))
        self.assertTrue(target.is_valid_position("a00"))
        self.assertTrue(target.is_valid_position("a25"))
        self.assertTrue(target.is_valid_position("p25"))

        self.assertFalse(target.is_valid_position("a26"))
        self.assertFalse(target.is_valid_position("a-0"))
        self.assertFalse(target.is_valid_position("a0-"))
        self.assertFalse(target.is_valid_position("a--"))
        self.assertFalse(target.is_valid_position("q23"))
        
    def test_is_not_same_position(self):
        target = IOUtils()
        self.assertTrue(target.is_not_same_position("a23","a25"))
        self.assertFalse(target.is_not_same_position("a23","a23"))
    
    def test_is_valid_letter_false(self):
        target = IOUtils()
        self.assertFalse(target.is_valid_letter("False"))
        self.assertFalse(target.is_valid_letter("false")) 

    def test_is_valid_number(self):
        target = IOUtils()
        self.assertFalse(target.is_valid_number("g"))
        self.assertFalse(target.is_valid_number("-1"))
        self.assertFalse(target.is_valid_number("26"))
        for i in range(0,26):
            self.assertTrue(target.is_valid_number(str(i)))
        
    def test_convert_letter(self):
        target = IOUtils()

        for i, c in enumerate(string.ascii_lowercase):
            self.assertEqual(i, target.convert_letter(c))
