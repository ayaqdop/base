import sys

BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"

RESET = "\033[0;0m"

class Console:

    def colored_print(self, text, color, end=''):
        sys.stdout.write(color)
        print(text, end=end)
        sys.stdout.write(RESET)