# PYnative Exercise 5:
# Given a list of numbers, return True if first and last number of a list is same


# First will generate a random list of numbers

import random

randomlist = []
for i in range (0,5):
    n = random.randint(1,10)
    randomlist.append(n)

print("This is your randomly generated list of 5 numbers: " + str(randomlist))

# Then will check of the first and last are the same

if randomlist[0] == randomlist[-1]:
    print("Result is True")
else:
    print("Result is False")