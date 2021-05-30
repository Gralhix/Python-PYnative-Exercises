# PYnative Exercise 4:
# Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
# https://pynative.com/python-basic-exercise-for-beginners/

# Note: I'm very aware that this is a slightly more complex way of solving the exercise. Creating slightly more complicated solutions helps me learn.


print("You'll be asked to provide a word and then a number. The number will define how many characters to remove from your word starting from the beginning")

yourword = input("Please give me your word:\n> ")
yournumber = int(input("Please give me your number:\n> "))

newword = yourword[yournumber:]

print(newword)
                   
