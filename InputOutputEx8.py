# https://pynative.com/python-input-and-output-exercise/
# Exercise 8: Format the following data using a string.format() method.
# Given: totalMoney = 1000 , quantity = 3 , price = 450
# Expected Output: I have 1000 dollars so I can buy 3 football for 450.00 dollars.


totalMoney = 1000
quantity = 3
price = 450

sentence = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars."
print(sentence.format(totalMoney, quantity, price))



