import re
import string


class IOUtils:


    def input_parser(self, input_value):
        input_value = re.split('\W+',input_value)
        current_pos = input_value[0]
        next_pos = input_value[1]
        #step = {}
        
        if (self.is_valid_position(current_pos)
            and self.is_valid_position(next_pos)
            and self.is_not_same_position(current_pos,next_pos)):
            step={
            'FROM':{'X': self.convert_letter(current_pos[0]), 'Y': int(current_pos[1:])},
            'TO':{'X': self.convert_letter(next_pos[0]), 'Y': int(next_pos[1:])}
            }
            return step
        else:
            return "Incorrect input"

    def is_not_same_position(self,pos1,pos2):
        return pos1 != pos2

    def is_valid_letter(self, letter):
        return len(letter)==1 and letter.isalpha() and "a" <= letter <= "p"

    def is_valid_number(self, number):
        return number.isnumeric() and 0 <= int(number) <= 25

    def is_valid_position(self, position):
        letter = position[0]
        number = position[1:]
        return self.is_valid_letter(letter) and self.is_valid_number(number)

    def convert_letter(self, letter):
        return ord(letter) - ord("a") + 1
