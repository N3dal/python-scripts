#!/usr/bin/python3
# -----------------------------------------------------------------
# this script will print the year number or any number in terminal,
# using the chan that you use example:
#
# ###########    ###########
#          ##    ##       ##
#          ##    ##       ##
# ###########    ##       ##
# ##             ##       ##
# ##             ##       ##
# ###########    ###########
#
#
# Author:N84.
#
# Create Date:Sun Dec 26 20:53:16 2021.
# ///
# ///
# ///
# -----------------------------------------------------------------


from os import system
from time import sleep
import random
import string


def clear():
    """function to wipe the terminal screen."""
    system("clear")


# wipe the terminal.
clear()


# create the numbers string.
numbers = [



    """##########
##      ##
##      ##
##      ##
##      ##
##      ##
##########""",

    """    ##     
  ## #     
##  ##     
    ##     
    ##     
    ##     
###########""",

    """##########
        ##
        ##
##########
##        
##        
##########""",

    """##########
        ##
        ##
##########
        ##
        ##
##########""",

    """##      ##
##      ##
##      ##
##########
        ##
        ##
        ##""",

    """##########
##        
##       
##########
        ##
        ##
##########""",

    """##########
##          
##       
##########
##      ##
##      ##
##########""",

    """##########
       ##
      ## 
     ##  
    ##    
   ##    
  ##""",

    """##########
##      ##
##      ##
##########
##      ##
##      ##
##########""",

    """##########
##      ##
##      ##
##########
        ##
        ##
##########"""



]


def generate_num(number: int = 2022, char: str = '#') -> str:
    """this function will print the number that you enter,
    to ascii characters on the terminal."""

    # guard condition.
    if not isinstance(number, int):
        # if the input was non-integer value.
        return -1

    # make sure that we use char only.
    # so if the input (char-variable) was string we will take only one,
    # char and its the first item.
    char = char[0]

    # note that any number as string is only seven lines.
    final_number = ""
    for line in range(7):
        # print(f"XXXXXXXXXXXXXXXXXXXXX(line number {line+1}")
        for num in str(number):
            final_number += numbers[int(num)
                                    ].split('\n')[line] + (' '*3)
            # print(final_number)
            # print()
            # print()
        final_number += '\n'

    # now use the replace method to change the character from '#' to the,
    # char var.
    return final_number.replace('#', char)


def animation_number(number: int = 2022):
    """this function will take a number and print as,
    characters like the print_num function with one,
    different and its this function will change the char,
    that used to view the number randomly and with that,
    we will get some nice effects."""

    # first we need to get the number as string.

    # guard condition
    if not isinstance(number, int):
        return -1

    num_string = generate_num(number, '#')
    choices = [*string.ascii_letters, *string.digits, *string.punctuation]
    while 1:
        clear()
        rep = '#' if '#' in num_string else random.choice(choices)
        num_string = num_string.replace(rep, random.choice(choices), 1)
        print(num_string)
        sleep(1e-2)


def main():
    # for num in numbers:
    #     print(num)
    # print(print_num(2022, '$$'))
    animation_number(2002)


if __name__ == "__main__":
    main()
