#PYnative Exercise 3:
#Given a string, display only those characters which are present at an even index number.
# https://pynative.com/python-basic-exercise-for-beginners/

# Note: I'm very aware that this is a slightly more complex way of solving the exercise. Creating slightly more complicated solutions helps me learn.


yourword = input("Please write a word. I will display the even characters.\n> ")
i=0
while i<len(yourword):
    print(yourword[i])
    i=i+2
