#!/usr/bin/env python3

# Created by Mr. Coxall
# Created on Nov 2020
# This program calculates the area and perimeter of a 15mm circle

import math


def main():
    # this function calculates the area and perimeter of a 15mm circle

    print("The perimeter of a 15 mm radius circle is {0}mm.".format(
           2 * math.pi * 15))
    print("The area of a 15 mm radius circle is {0}mm².".format(
           math.pi * 15**2))


if __name__ == "__main__":
    main()
