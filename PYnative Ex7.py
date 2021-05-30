# PYnative Exercise 7:
# Return the count of sub-string “Emma” appears in the given string
# https://pynative.com/python-basic-exercise-for-beginners/

# Note: I'm very aware that this is a complicated way of solving the exercise. Creating slightly more complicated solutions helps me learn.


# Will create a list of 5 names from 3 possibilities

import random

listofnames = ["Emma", "Magda", "Diana"]

newnamelist = []
for i in range (0,5):
    name = random.choice(listofnames)
    newnamelist.append(name)                 

#print("DEBUG This are your list of 5 names: " + str(newnamelist))

# Will create 5 sentences with the select names above

listofsentences = [" is a nice person.\n ", " is great at painting.\n ", " is trying to learn python.\n ", " is an international spy.\n ", " is making a chicken coop.\n "]

fullsentence = [a + b for a, b in zip(newnamelist, listofsentences)]

#print("DEBUG This is the sentence list: " + str(fullsentence))


# Convert list to string. Don't know why the first sentence is not alligned with the others but doesn't change the output.

listtostr = "".join([str(element) for element in fullsentence])
print(listtostr)


# Will then count how many times "Emma" was mentioned in string

emmaword = "Emma"
count = listtostr.count(emmaword)
print("The word 'Emma' appeared "+ str(count) + " time(s) in the sentences above.")
