# https://pynative.com/python-input-and-output-exercise/
# Exercise 4: Display float number with 2 decimal places using print()


n = float(input("Please provide a number with at least 3 decimal places:\n > "))
nd = "{:.2f}".format(n)
print("This is your number with only 2 decimal places: ", nd)