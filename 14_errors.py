"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
print("--------Example 1: Division--------")
print()
print()

def divide_numbers(num1, num2):
    result = num1 / num2
    print("Result:", result)

# Example usage:
try:
    divide_numbers(10, 0)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

print()
print()
print("--------Example 1: Division--------")
print()


"""
Example 2: Opening Files
"""
print("--------Example 2: Opening Files--------")
print()
print()

def read_file(filename):
    file = open(filename, 'r')
    contents = file.read()
    print("File contents:", contents)
    file.close()

# Example usage:
try:
    read_file("nonexistent.txt")
except FileNotFoundError:
    print("Error: File not found.")

print()
print()
print("--------Example 2: Opening Files--------")
print()


"""
Example 3: List Items
"""
print("--------Example 3: List Items--------")
print()
print()

def get_item(lst, index):
    item = lst[index]
    print("Item:", item)

# Example usage:
try:
    my_list = [1, 2, 3]
    get_item(my_list, 5)

except IndexError:
    print("The index you are trying to access is out of range.")

print()
print()
print("--------Example 3: List Items--------")
print()

"""
Example 4: Dictionaries
"""
print("--------Example 4: Dictionaries--------")
print()
print()

def get_value(dictionary, key):
    value = dictionary[key]
    print("Value:", value)

# Example usage:
my_dict = {"a": 1, "b": 2}

try:
    get_value(my_dict, "c")

except KeyError:
    print("The key you are trying to access doen't exist in the dictionary.")

print()
print()
print("--------Example 4: Dictionaries--------")
print()

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        print("Finished attempting to process the file.")

# Example usage:
process_file("example.txt")

print()
print()
print("--------Example 5: Else/Finally--------")
print()
