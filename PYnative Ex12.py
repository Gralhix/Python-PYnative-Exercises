# PYnative Exercise 12:
# Calculate income tax for the given income by adhering to the below rules
# Taxable Income | Rate (in %)
# First $10,000 | 0
# Next $10,000 | 10
# The remaining | 20

# https://pynative.com/python-basic-exercise-for-beginners/

# Note: I'm very aware that this exercise did not require user input. Creating slightly more complicated solutions helps me learn.


income = input("What's your annual income? > ")

print(income)

income = int(income)

if income > 10000 and income < 20000:
    tax = (income - 10000) * 10 /100
elif income > 20000:
    tax = 10000 * 10 /100
    tax += (income - 20000) * 20 / 100
else:
    tax = 0
    
# Line of code below is just so the result doesn't show as a float (6000.0 vs 6000)    
tax = int(tax)
    
print("Total tax to pay is: " + str(tax))