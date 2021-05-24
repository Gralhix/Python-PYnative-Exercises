#PYnative Exercise 1
#Given two integer numbers return their product. If the product is greater than 1000, then return their sum

firstnumber = int(input("first number?\n"))
secondnumber = int(input("second number?\n"))

if (firstnumber * secondnumber) > 1000:
    print(firstnumber + secondnumber)
else:
    print(firstnumber * secondnumber)