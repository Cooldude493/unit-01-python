#Welcome to the Calculatinator-inator 9000!

#Enter the first number: 10
#Enter the second number: 5

#Select operation:
#1. Addition
#2. Subtraction
#3. Multiplication
#4. Division
#5. Floor Division
#6. Exponential
#7. Remainder

#Enter choice: 3

#Result: 50.0


print("Welcome to the Calculatinator-inator 10000! ... Our 9000 model tried to divide by zero and blew up.")

addition = 1
subtraction = 2
multiplication = 3
division = 4
floor_division = 5
exponential = 6
remainder = 7  # 22-28 created variable for each operation



num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder") 
print()
operation = int(input("What operation would you like to perform? Enter the number corrosponding with the operation.: "))
# 32-43 prompt the user dor inputs depicting their numbers and operation choice 


if operation == addition:
    result = num1 + num2
    print(f"Result: {result}")

elif operation == subtraction:
    result = num1 - num2
    print(f"Result: {result}")

elif operation == multiplication:
    result = num1 * num2
    print(f"Result: {result}")

elif operation == division:
    if num2 == 0:
        print("Error: Division by zero is not allowed. Hey no.")
    else:
        result = num1 / num2
        print(f"Result: {result}")

elif operation == floor_division:
    if num2 == 0:
        print("Error: Division by zero is not allowed. Nope.")
    else:
        result = num1 // num2
        print(f"Result: {result}")

elif operation == exponential:
    result = num1 ** num2
    print(f"Result: {result}")

elif operation == remainder:
    if num2 == 0:
        print("Error: Division by zero is not allowed. Abolutly not.")
    else:
        result = num1 % num2
        print(f"Result: {result}") # 47-82 if and elif statments to perform the correct operation based on the users input

if operation >= 8 or operation <= 0:
    print("Error: Invalid operation choice. Please select a number between 1 and 7.") # 84-85 error message for invalid operation choice
 