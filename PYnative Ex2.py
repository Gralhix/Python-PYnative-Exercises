#PYnative Exercise 2:
#Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number
# https://pynative.com/python-basic-exercise-for-beginners/

# Note: I'm very aware that this is a slightly more complex way of solving the exercise. Creating slightly more complicated solutions helps me learn.


print("Printing current and previous number sum in a range(10):\n")
previousnumber = 0
for i in range(10):
    currentnumber = i
    sums = i + previousnumber
    print("Current Number: " + (str(i)) + " -- Previous Number " + (str(previousnumber)) + " -- Sum: " + (str(sums)))
    previousnumber = i
