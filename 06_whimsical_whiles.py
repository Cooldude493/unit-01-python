"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
print("--------Exercise 1--------")
print()
print()
i = 1
while i <= 10:
    print(i)
    i += 1 # Made a loop that prints numbers from 1 to 10
print()
print()
print("--------Exercise 1--------")
print()

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

print("--------Exercise 2--------")
print()
print()
j = 10
while j >= 1:
    print(j)
    j -= 1 # Made a loop that prints numbers from 10 to 1
print()
print()
print("--------Exercise 2--------")
print()


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
print("--------Exercise 3--------")
print()
print()
num = int(input("Enter a number to calculate its factorial: "))
factorial = 1
while num > 0:
    factorial *= num # Each iteration increases the factorial then decreases the number by 1 in which they are multiplied by each other
    num -= 1
print(f"Factorial: {factorial}") # Calculated the factorial of a number given by the user
print()
print()
print("--------Exercise 3--------")
print()

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
print("--------Exercise 4--------")
print()
print()
password = "qwerty"
user_guess = ""
while user_guess != password:
    user_guess = input("Guess the password: ")
    if user_guess == password:
        print("Access Granted!")
    else:
        print("Incorrect password, try again.") # Made a loop that keeps asking the user to guess the password until they get it right
print()
print()
print("--------Exercise 4--------")
print()
"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
#SKIPPED


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

print("--------Exercise 6--------")
print()
print()
n = int(input("Enter the number of Fibonacci numbers to generate: "))

a = 0 
b = 1

while n > 0:
    print(a)
    a, b = b, a + b
    n -= 1 # Generated the amount of Fibonacci numbers the user requested
print()
print()
print("--------Exercise 6--------")
print()