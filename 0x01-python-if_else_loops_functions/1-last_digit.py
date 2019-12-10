#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is ".format(number), end="")
if number < 0:
    t = (number * -1) % 10
else:
    t = number % 10
if number < 0:
    t = t * -1
if t == 0:
    print('{} and is 0'.format(t))
elif t > 5:
    print('{} and is greater than 5'.format(t))
elif t < 6:
    print('{} and is less than 6 and not 0'.format(t))
