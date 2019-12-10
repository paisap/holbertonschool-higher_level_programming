#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is".format(number), end=" ")
if number < 0:
    t = (number * -1) % 10
else:
    t = number % 10
if number < 0:
    t = t * -1
if t == 0:
    print('0 and is 0')
if t > 5:
    print('{} and is greater than 5'.format(t))
else:
    print('{} and is less than 6 and not 0'.format(t))
