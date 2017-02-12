import unittest
import sys

sys.path.insert(0, "home/ayaqdop/base")

import console

class ConsoleTest(unittest.TestCase):

    def test_colored_print(self):
        self.assertEqual("\033[1;30m", prettyprint.BLACK)
        self.assertEqual("\033[1;31m", prettyprint.RED)
        self.assertEqual("\033[1;32m", prettyprint.GREEN)
        self.assertEqual("\033[1;33m", prettyprint.YELLOW)
        self.assertEqual("\033[1;34m", prettyprint.BLUE)
        self.assertEqual("\033[1;35m", prettyprint.MAGENTA)
        self.assertEqual("\033[1;36m", prettyprint.CYAN)
        self.assertEqual("\033[1;37m", prettyprint.WHITE)

