# https://pynative.com/python-input-and-output-exercise/
# Exercise 5: Accept a list of 5 float numbers as an input from the user


print("This code will create a list of 5 floats provided by the user")
flist = []
for i in range(0,5):
    n = float(input("Please provide a float: "))
    flist.append(n)
print("Here is a list made of the 5 floats you provided: ", flist)
