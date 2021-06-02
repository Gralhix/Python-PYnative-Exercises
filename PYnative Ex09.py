# PYnative Exercise 9:
# Reverse a given number and return true if it is the same as the original number
# https://pynative.com/python-basic-exercise-for-beginners/

# Will generate a random number between 100 and 999

import random

num = random.randint(100,1000)
print(num)
digit = (str(num))

# Will check if the first and third numbers are the same

if digit[0] == digit[2]:
    print("The number is the same when reversed")
else:
    print("The number is  not the same when reversed")
