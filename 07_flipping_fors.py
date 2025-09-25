"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print("--------Exercise 1--------")
print()
print()
my_sting = "Hello, World!"
for char in my_sting:
    print(char)  # Printed each character in the string "Hello, World!"
print()
print()
print("--------Exercise 1--------")
print()

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print("--------Exercise 2--------")
print()
print()
my_list = [1, 2, 3, 4, 5]
total = 0
for num in my_list:
    total += num  # Calculated the sum of elements in the list
print("Sum:", total)
print()
print()
print("--------Exercise 2--------")
print()

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print("--------Exercise 3--------")
print()
print()
animals = ["cat", "elephant", "giraffe", "hippopotamus"]
for animal in animals:
    print(f"{animal}: {len(animal)}")  # Printed the length of each word in the list
print()
print()
print("--------Exercise 3--------")
print()


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

print("--------Exercise 4--------")
print()
print()
my_dict = {"name": "Jason", "age": 18, "city": "New York", "occupation": "Student"}
for key in my_dict:
    print(f"{key}")  # Printed each key-value pair in the dictionary
#The output wasnt what i expected as it only printed the keys and not the values
print()
print()
print("--------Exercise 4--------")
