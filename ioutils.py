import re

def input_parser():
    input_value = input("Enter positions: ")
    player_move = re.split('\W+',input_value)
        

    print (player_move)
        

input_parser()
