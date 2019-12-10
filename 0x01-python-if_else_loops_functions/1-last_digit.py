#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is".format(number), end=" ")
t = number
if t < 0:
    t = t * -1
if t % 10 == 0:
    if number < 0:
        print('-', end="")
    print('0 and is 0'.format(t % 10))
elif t % 10 > 5:
    if number < 0:
        print('-', end="")
    print('{} and is greater than 5'.format(t % 10))
else:
    if number < 0:
        print('-', end="")
    print('{} and is less than 6 and not 0'.format(t % 10))
