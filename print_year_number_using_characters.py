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


def print_num(number: int = 2022, char: str = '#'):
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


def main():
    # for num in numbers:
    #     print(num)
    print(print_num(2022, '$$'))


if __name__ == "__main__":
    main()
