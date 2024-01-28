#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
if number > 5:
    print("Last digit of " + str(number) + " is " + number_str[-1] + "and is greater than 5")
elif number < 6 and number != 0 :
    print("Last digit of " + str(number) + " is " + number_str[-1] + " and is less than 6 and not 0")
else:
    print("Last digit of " + str(number) + " is " + number_str[-1] + " and is 0")