"""
TASK 1:
Count how many spaces are in a given string
"""

print("--------Task 1--------")
print()
print()

text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":
       count += 1

print(count)

print()
print()
print("--------Task 1--------")
print()

"""
Task 2:
Determine if numbers 1 to n are even or odd 
"""
print("--------Task 2--------")
print()
print()

print("give me a number")
n = int(input())

for num in range(1, n):
    if num % 2 <= 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

print()
print()
print("--------Task 2--------")
print()

"""
Task 3:
Calculate the factorial of a given number
"""

print("--------Task 3--------")
print()
print()

num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num + 1):
    result *= i   

  print(f"Factorial of {num} is {result}") 

print()
print()
print("--------Task 3--------")
print() 

"""
Task 4:
Ask user to enter the correct password but only give them 3 attempts
"""

print("--------Task 4--------")
print()
print()

attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts == 3:
        print("Too many attempts")
        break

print()
print()
print("--------Task 4--------")