import re
import string


class IOUtils:

    def input_parser(self, input_value):
        input_value = re.split("\W+", input_value)
        current_position = input_value[0]
        next_position = input_value[1]
        if (self.is_valid_position(current_position)
            and self.is_valid_position(next_position)
            and self.is_not_same_position(current_position, next_position)):
            return {
                "FROM" : self.get_coordinate(current_position),
                "TO" : self.get_coordinate(next_position)
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
