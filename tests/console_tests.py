import io
from unittest import TestCase
from contextlib import redirect_stdout
import console


class ConsoleTest(TestCase):
    def test_colored_print_constants(self):
        self.assertEqual("\033[1;30m", console.BLACK)
        self.assertEqual("\033[1;31m", console.RED)
        self.assertEqual("\033[1;32m", console.GREEN)
        self.assertEqual("\033[1;33m", console.YELLOW)
        self.assertEqual("\033[1;34m", console.BLUE)
        self.assertEqual("\033[1;35m", console.MAGENTA)
        self.assertEqual("\033[1;36m", console.CYAN)
        self.assertEqual("\033[1;37m", console.WHITE)

    def test_colored_print(self):
        target = console.Console()
        stream = io.StringIO()

        with redirect_stdout(stream):
            target.colored_print("Hello, World!", color=console.RED)

        self.assertEqual(console.RED + "Hello, World!" + console.RESET, stream.getvalue())
