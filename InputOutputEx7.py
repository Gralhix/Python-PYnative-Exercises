# https://pynative.com/python-input-and-output-exercise/
# Exercise 7: Accept any three string from one input() call


words = input("Please enter 3 words separated by spaces: ")
if words.count(" ") == 2: 
    print(words)
else:
    print("Those were not 3 words separated by a space each")