import random

number = random.randint(-10, 10)

print(f"{number} is {'positive' if number > 0 else 'zero' if number == 0 else 'negative'}")