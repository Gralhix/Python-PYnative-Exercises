# PYnative Exercise 10:
# Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list
# https://pynative.com/python-basic-exercise-for-beginners/

# Note: I'm very aware that I did not need to create the random lists to solve the exercise. Creating slightly more complicated solutions helps me learn.

import random

# Will create the first list with 5 random numbers

firstlist = []
for i in range (0,5):
    n = random.randint(1,51)
    firstlist.append(n)

# Will create the second list with 5 random numbers

secondlist = []
for i in range (0,5):
    n = random.randint(1,51)
    secondlist.append(n)    
    
finallist = []

# Will check which item from the first list is an odd number and append to the final list

for item in firstlist:
    if item % 2 != 0:
        finallist.append(item) 

# Will check which item from the second list is an even number and append to the final list

for item in secondlist:
    if item % 2 == 0:
        finallist.append(item) 

# Will print all three lists

print("First list: " + str(firstlist))
print("Second list: " + str(secondlist))
print("Final list: " + str(finallist))
