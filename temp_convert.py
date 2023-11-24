#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: November 24, 2023
# This program calculates temperature in celsius to fahrenheit


def temp_convert():
    # get length and width
    print("Converting temperature in celsius to fahrenheit")
    temp_celsius = int(input("What is the temperature in celsius?"))

    # calculate temperature in fahrenheit
    temp_fahrenheit = 9 / 5 * temp_celsius + 32

    # display tThe temperature in fahrenheit
    print("The temperature in fahrenheit is {} F°".format(temp_fahrenheit))


def main():
    # call the temp_convert() function
    temp_convert()


if __name__ == "__main__":
    main()
