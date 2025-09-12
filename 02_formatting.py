"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
("--------Task 1--------")
print()
print()
password = "Apple"
user_input = input("Enter the password: ")
if user_input.lower() == password.lower():
    print("Access granted")
elif user_input == password.upper():
    print("Access granted")
else:
    print("Access denied") # Codded to check if the inputed password is correst regardless of case sensitivity
print()
print()
print("--------Task 1--------")
print()
"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
print("--------Task 2--------")
print()
print()
user_input = input("Enter a string: ")
if user_input == "":
    print("invalid")
elif user_input.strip() == "":
    print("invalid")
else:
    print("valid") # Codded to check if the inputed string is empty or contains only spaces and prints "invalid" if its only spaced or empty and "valid" if it contains any characters
print()
print()
print("--------Task 2--------")
print()


"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
print("--------Task 3--------")
print()
print()
user_input = input("Enter the word cat: ")
print(user_input.replace("cat", "dog").replace("Cat", "Dog").replace("CAT", "DOG")) 
print("silly thats not a cat") # Codded to replace all occurances of the word "cat" with "dog" regardless of capitalization
print()
print()
print("--------Task 3--------")
print()

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
print("--------Task 4--------")
print()
print()
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"{name} is {age} years old") # Codded to take a person's name and age as input and prints it in a string
print()
print()
print("--------Task 4--------")
print()

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
print("--------Task 5--------")
print()
print()
num1 = float(input("Enter the first float: "))
num2 = float(input("Enter the second float: "))
quotient = num1 / num2
print(f"The quotient is {quotient:.1f}") # Made an input of two floats and divided them and printed the result rounded to the nearest tenth
print()
print("--------Task 5--------")