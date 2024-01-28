#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_digit = int(number_str[-1])
if number < 0 :
	last_digit = last_digit * (-1)
if last_digit > 5:
    print("Last digit of " + str(number) + " is " + number_str[-1] + "and is greater than 5")
elif last_digit < 6 and last_digit != 0 :
    print("Last digit of " + str(number) + " is " + number_str[-1] + " and is less than 6 and not 0")
else:
    print("Last digit of " + str(number) + " is " + number_str[-1] + " and is 0")