#!/usr/bin/python3
# -----------------------------------------------------------------
# this script will calculate the largest square,
# that we can fit inside circle with any radius.
#
#
#
# Author:N84.
#
# Create Date:Thu Dec 16 20:53:03 2021.
# ///
# ///
# ///
# -----------------------------------------------------------------
from os import system


def clear():
    """wipe the terminal screen"""
    system("clear")


def find_size_of_square(radius: float):
    """calculate the largest square can fit inside,
    circle with radius r with this formula:
    let's assume the one side of the square is 'a', 
    and in this case the length of 'a' will equal to:
    [a=sqrt(2)*r].
    and to calculate the square size we know its,
    equal to [a^2] and that equal to:
    [a^2=2*r^2].
    and by that we can calculate the largest square we can fit in circle.
    note: remember 'r' not equal to 'R.
    remember [R=2r], so when try to prove the previous formula,
    remember that."""

    return 2*radius**2


def main():
    square_size = find_size_of_square(5)
    print(f"{square_size=}")


if __name__ == "__main__":
    main()
