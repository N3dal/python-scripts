#!/usr/bin/python3
"""
simple script that will tell you the operation that,
happen between two numbers by giving it the result.

"""

from os import system


def clear():
    """wipe the terminal screen"""
    system("clear")


clear()


def main():
    msg = "Enter num1 and num2 and result: "
    number1, number2, res = [float(num) for num in input(msg).split()]

    operators = ['+', '-', 'x', '/']

    operations = [
        number1+number2 == res,
        number1-number2 == res,
        number1*number2 == res,
        number1/number2 == res,
    ]

    print("The operation is: ", end='')
    # make sure that we return a correct value to the user.
    # note index will raise an error if didn't find the item.
    opr = operators[r.index(True)] if any(operations) else "Non-sense"
    print(opr)


if __name__ == "__main__":
    main()
