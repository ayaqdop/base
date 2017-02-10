import unittest
import sys

sys.path.insert(0, "home/ayaqdop/base")

from prettyprint import PrettyPrint

class PrettyPrintTest(unittest.TestCase):

    def test_colored_print(self):
        target = PrettyPrint()

        target.colored_print("Text", "RED")