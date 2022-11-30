#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
tempNum = number

if number < 0:
    number = -(number)

last_digit = number % 10
if tempNum < 0:
    number = tempNum
    last_digit = -(last_digit)

if last_digit > 5:
    string = "and is greater than 5"

if last_digit == 0:
    string = "and is 0"

if last_digit < 6 and last_digit != 0:
    string = "and is less than 6 and not 0"

print("Last digit of " + str(number) + " is " +
    str(last_digit) + " " + string)
print("\n")