import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

output_string = f"Last digit of {number} is {last_digit} and is"
if last_digit > 5:
    output_string += " greater than 5"
elif last_digit == 0:
    output_string += " 0"
else:
    output_string += " less than 6 and not 0"

print(output_string)