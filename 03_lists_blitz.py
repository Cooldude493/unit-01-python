"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
print("--------Task 1--------")
print()
print()
my_list = ["apple", False, 123, 12.2]
print(my_list) # Created a list with 4 elements and printed it
print()
print()
print("--------Task 1--------")
print()

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
print("--------Task 2--------")
print()
print()
my_list.append("banana") 
print(my_list) # Added an element to the end of the list and printed it
print()
print()
print("--------Task 2--------")
print()

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
print("--------Task 3--------")
print()
print()
my_list.remove("apple")
print(my_list) # Removed a specific element from the list and printed it
print()
print()
print("--------Task 3--------")
print()

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
print("--------Task 4--------")
print()
print()
my_list[1] = "456"
print(my_list) # Modified the element 123 at index 2 with a new value 456 and printed the updated list
print()
print()
print("--------Task 4--------")
print()

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
print("--------Task 5--------")
print()
print()
my_list.append("strawberry")
my_list.append(789)
my_list.append(True)
print(my_list) # Appended the elements "strawberry", 789, and True to the end of the list and printed the updated list
print()
print()
print("--------Task 5--------")
print()

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
print("--------Task 6--------")
print()
print()
del my_list[3]
print(my_list) # Deleted the element 12.2 at index 3 and printed the updated list
print()
print()
print("--------Task 6--------")
print()


"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
print("--------Task 7--------")
print()
print()
new_list = my_list[0:2]
print(new_list) # Created a new variable equal to the first 2 items of my_list and printed it
print()
print()
print("--------Task 7--------")
print()

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
print("--------Task 8--------")
print()
print()
other_list = [101, "dragonfruit", 99.23]
total_list = my_list + other_list
print(total_list) # Extended my_list with the elements of other_list and printed the updated list
print()
print()
print("--------Task 8--------")