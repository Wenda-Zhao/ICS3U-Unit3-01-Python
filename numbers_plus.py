#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Nov 2020
# This program calculates numbers plus


def main():
    # this function calculates numbers plus

    # input
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the first number: "))

    # process
    answer = first_number + second_number

    # output
    print("")
    print("The answer is {0:,.0f} + {1:,.0f} = {2:,.0f}"
          .format(first_number, second_number, answer))


if __name__ == "__main__":
    main()
