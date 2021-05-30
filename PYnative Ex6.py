# PYnative Exercise 6:
# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
# https://pynative.com/python-basic-exercise-for-beginners/

# Note: I'm very aware that this is a slightly more complex way of solving the exercise. Creating slightly more complicated solutions helps me learn.


# First will generate a random list of numbers (bit of code done for exercise 5 with minor alterations)

import random

randomlist = []
for i in range (0,10):
    n = random.randint(1,61)
    randomlist.append(n)

print("This is your randomly generated list of 10 numbers: " + str(randomlist))


# Second part will iterate and print the ones that are divisible by 5

for x in range (len(randomlist)):
    if (randomlist[x]) % 5 == 0:
        print(randomlist[x])
 
