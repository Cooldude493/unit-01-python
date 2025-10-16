"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
print("--------Task 1--------")
print()
print()

def greet(name):
    """Takes a name as the argument and returns it as a greeting message."""
    return f"Hello, {name}!"

print(greet("Dave")) 
print()
print(greet("John")) # names as agruments for the function


print()
print()
print("--------Task 1--------")
print()

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
print("--------Task 2--------")
print()
print()

def square(num):
    """Takes an integer as an argument and returns its square."""
    return num ** 2

print(square(4))
print()
print(square(10)) # integers as agruments for the function

print()
print()
print("--------Task 2--------")
print()



"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
print("--------Task 3--------")
print()
print()

def is_even(num):
    """Takes a number as an argument and returns True if the number is even, and False otherwise."""
    return num % 2 == 0

print(is_even(4)) 
print()
print(is_even(11)) #Numbers that test if they are even or odd

print()
print()
print("--------Task 3--------")
print()

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
print("--------Task 4--------")
print()
print()

def area (length, width):
    """Takes the length and width of a rectangle and returns its area."""
    return length * width

print(area(5, 10))
print()
print(area(7, 3)) # length and width as agruments for the function

print()
print()
print("--------Task 4--------")
print()

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print("--------Task 5--------")
print()
print()

def cel_to_fah(celsius):
    """Takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit."""
    return (celsius * 9/5) + 32

print(cel_to_fah(0))
print()
print(cel_to_fah(43)) # Celsius temperatures as agruments for the function

print()
print()
print("--------Task 5--------")
print()

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
print("--------Task 6--------")
print()
print()
def average(numbers):
    """Takes a list of numbers as an argument and returns the average (mean) of those numbers."""
    return sum(numbers) / len(numbers)

print(average([10,12,24,11]))
print()
print(average([5,32,4,2,0])) # lists of numbers as agruments for the function

print()
print()
print("--------Task 6--------")
print()

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
print("--------Task 7--------")
print()
print()

def price_calc(price, quantity, discount=0):
    """Calculates the total price with an optional discount."""
    total = price * quantity
    if discount:
        total -= total * discount
    return total

print(price_calc(10, 5))
print()
print(price_calc(20, 3, 0.1)) # price and quantity as agruments for the function, with an optional discount

print()
print()
print("--------Task 7--------")