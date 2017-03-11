import re
import string


class IOUtils:

    def input_parser(self, input):
        current, next = re.split("\W+", input)
        if (self.is_valid_position(current)
            and self.is_valid_position(next)
            and self.is_not_same_position(current, next)):
            return {
                "FROM" : self.get_coordinate(current),
                "TO" : self.get_coordinate(next)
            }
        else:
            return None

    def get_coordinate(self, position):
        return {
            "X": self.convert_letter(position[0]),
            "Y": int(position[1:])
        }

    def is_not_same_position(self, position1, position2):
        return position1 != position2

    def is_valid_letter(self, letter):
        return len(letter) == 1 and letter.isalpha() and "a" <= letter <= "p"

    def is_valid_number(self, number):
        return number.isnumeric() and 0 <= int(number) <= 25

    def is_valid_position(self, position):
        letter = position[0]
        number = position[1:]
        return self.is_valid_letter(letter) and self.is_valid_number(number)

    def convert_letter(self, letter):
        return ord(letter) - ord("a") + 1
