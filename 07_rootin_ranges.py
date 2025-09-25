"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print("--------Exercise 1--------")
print()
print()
for i in range(1, 11): 
    print(i) # Printed numbers from 1 to 10
print()
print()
print("--------Exercise 1--------")
print()


"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print("--------Exercise 2--------")
print()
print()
for i in range(900, 1001, 10):
    print(i) # Counted by 10s from 900 to 1000
print()
print()
print("--------Exercise 2--------")
print()

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print("--------Exercise 3--------")
print()
print()
for i in range(1, 101, 9):
    print(i) # Counted from 1 to 100 by 9s
print()
print()
print("--------Exercise 3--------")
print()

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print("--------Exercise 4--------")
print()
print()
total = 0
for i in range (1, 11):
    total += i # Calculated the sum of all numbers from 1 to 10
print("Sum:", total) 
print()
print()
print("--------Exercise 4--------")
print()

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5
 
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

    #The output is only stars printed in a line with each line having one more star than the previous line
    #The loop iterates through the range of rows which is 5 and prints a star for each iteration it goes through