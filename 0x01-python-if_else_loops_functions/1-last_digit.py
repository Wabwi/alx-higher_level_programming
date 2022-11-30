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

print("Last digit of " + str(number) + " is " + str(last_digit), end=' ' )

if last_digit > 5:
    print(" and is greater than 5")

if last_digit == 0:
    print(" and is 0")

if last_digit < 6 and last_digit != 0:
    print(" and is less than 6 and not 0")
