# :)

"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
print("--------Task 1--------")
print()
print()
x = 35.24
int(x)
print(x)
print(int(x)) # Changed the varriable X to int(x) to print the converted integer
print()
print()
print("--------Task 1--------")
print()
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
print("--------Task 2--------")
print()
print()
y = float(input("Enter a number: "))
if y > 0:
    print("The number is positive.")
elif y < 0:
    print("The number is negative.")
else:
    print("The number is zero.") # Made if/else/elif statements to check if the number is positive, negative or zero
print()
print()
print("--------Task 2--------")
print()


"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
print("--------Task 3--------")
print()
print()
z = int(input("Enter an integer: "))
w = float(input("Enter a float: "))
print(f"Addition: {z + w}")
print(f"Subtraction: {z - w}")
print(f"Multiplication: {z * w}")
print(f"Division: {z / w}") # Created an input for an integer and a float that then printed out the addition, subtraction, multiplication and division of the two numbers
print()
print()
print("--------Task 3--------")
print()
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
print("--------Task 4--------")
print()
print()
fruits = {
    "Blueberry": 10,
    "Strawberry": 12,
    "Orange": 5
}
print(fruits["Strawberry"]) # Created a dictionary with fruit names as well as their quantities and printed out the quantity of strawberries
print()
print()
print("--------Task 4--------")
print()

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
print("--------Task 5--------")
print()
print()
q = "1, 2, 3, 4, 5"
tuple(q.split(", "))
print(q)
print(tuple(q.split(", "))) # Created a string variable with a list of numbers and converted that string into a tuple and printed both the original string and the tuple
print()
print()
print("--------Task 5--------")
print()
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""
print("--------Task 6--------")
print()
print()

Subjects = ["Math", "Science", "History", "English"]
my_string = ", ".join(Subjects)
my_string2 = " - ".join(Subjects)
print(Subjects)
print(my_string)
print(my_string2) # Created a list of subjects and used the join function to combine them into a single string separated by commas and " - " as the separator and printed both the original and both strings
print()
print()
print("--------Task 6--------") 