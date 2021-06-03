# PYnative Exercise 11:
# Write a code to extract each digit from an integer, in the reverse order
# https://pynative.com/python-basic-exercise-for-beginners/

import random

# Will create a 4 digit random number

num = random.randint(1000,10000)
print("The number is: " + str(num))

# Will print the number reversed and with spaces in between each digit

strnum = str(num)

print("The reverse number is: " + strnum[3] + " " + strnum[2] + " " + strnum[1] + " " + strnum[0])