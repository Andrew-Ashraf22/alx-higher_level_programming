#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_d = abs(number) % 10
    last_d = -last_d
else:
    last_d = number % 10
if last_d == 0:
    print("Last digit of {} is {} and is 0".format(number, last_d))
elif last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
