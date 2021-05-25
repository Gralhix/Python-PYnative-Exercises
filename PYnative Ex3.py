#PYnative Exercise 3:
#Given a string, display only those characters which are present at an even index number.

yourword = input("Please write a word. I will display the even characters.\n> ")
i=0
while i<len(yourword):
    print(yourword[i])
    i=i+2
