# PYnative Exercise 15:
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# https://pynative.com/python-basic-exercise-for-beginners/


#Case 1:
def exponent(base, exp):
    result = base**exp
    print("Base = " + str(base))
    print("Exponent = " + str(exp))
    print(str(base) + " raised to the power of " + str(exp) + ": " + str(result))
    print("\t")
exponent(2, 5)



#Case 2:
def exponent(base, exp):
    result = base**exp
    print("Base = " + str(base))
    print("Exponent = " + str(exp))
    print(str(base) + " raised to the power of " + str(exp) + ": " + str(result))
    print(result)
    
exponent(5, 4)
