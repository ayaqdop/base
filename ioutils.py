import re
import string


class IOUtils:


    def input_parser(self):
        input_value = re.split('\W+',input("Enter positions: "))
        
        if(input_value[0] == input_value[1] 
            or not input_value[0][0] in 'abcdefghijklmnopABCDEFGHIJKLMNOP' 
            or not input_value[1][0] in 'abcdefghijklmnopABCDEFGHIJKLMNOP'
            or input_value[0][1:].isalpha()
            or input_value[1][1:].isalpha()
            or len(input_value[0])>3
            or len(input_value[1])>3
            or not int(input_value[0][1:]) >=0
            or not int(input_value[0][1:]) <=25
            or not int(input_value[1][1:]) >=0
            or not int(input_value[1][1:]) <=25):
            print("Something wrong with your values, please retype your player and move position: ")
            input_parser()
        else:
            input_value[0] = input_value[0][0].lower()+input_value[0][1:]
            input_value[1] = input_value[1][0].lower()+input_value[1][1:]
            print(input_value[0], input_value[1])
            #current pos = {curX:input_value[0][0], curY:input_value[0][1:]}

    def is_not_same_position(self, pos1,pos2):
        return pos1 != pos2
            
    def is_valid_letter(self, letter):
        letter = letter.lower()
        return len(letter)==1 and letter.isalpha() and "a" <= letter <= "p"

    def is_valid_number(self, number):
        return number.isnumeric() and 0 <= int(number) <= 25

    def is_valid_position(self, position):
        letter = position[0]
        number = position[1:]
        return is_valid_letter(letter) and is_valid_number(number)
            

