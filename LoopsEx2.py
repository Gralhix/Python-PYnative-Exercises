# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# Python if else, for loop, and range() Exercise with Solutions
# Exercise 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')