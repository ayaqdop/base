import re
import string

def input_parser():
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



input_parser()