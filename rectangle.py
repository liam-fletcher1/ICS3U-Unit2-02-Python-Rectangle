#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program calculates the area and perimeter of a circle
#    with radius inputted from the user

import math


def main():
    # this function calculates the area and perimeter of a rectangle

    # input
    Length = int(input("Enter Length of the rectangle (mm):"))
    width = int(input("Enter width of the rectangle (mm):"))

    # process
    area = Length * width
    perimeter = 2 * (Length + width)

    # output
    print("")
    print("Area is {0}mm².".format(area))
    print("perimeter is {0}mm.".format(perimeter))


if __name__ == "__main__":
    main()
