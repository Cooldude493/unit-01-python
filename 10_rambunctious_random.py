import random

"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""

print("--------Task 1--------")
print()
print()

total = 0

while total < 10:
    roll = random.randint(1, 6)
    print("Roll:", roll)
    total += 1 #A simulation that rolls a six-sided die 10 times and prints each result.

print()
print()
print("--------Task 1--------")
print()

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
print("--------Task 2--------")
print()
print()

total = 0

while total < 5:
    num = random.uniform(0, 1)
    print("Random float between 0 and 1:", num)
    total += 1 # Generate 5 random floating-point numbers between 0 and 1
print()
while total < 10:
    num = random.uniform(10, 20)
    print("Random float between 10 and 20:", num)
    total += 1 # Generate 5 random floating-point numbers between 10 and 20

print()
print()
print("--------Task 2--------")
print()

"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
print("--------Task 3--------")
print()
print()

colors = ["red", "blue", "green", "yellow", "purple"]

selected_colors = random.choices(colors, k=3)
print("Selected colors:", selected_colors) # Randomly select and print 3 colors from the list

print()
print()
print("--------Task 3--------")
print()


"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""

print("--------Task 4--------")
print()
print()

numbers = list(range(1, 11))
print("Original numbers:", numbers)
print()
shuffle = random.shuffle(numbers)
print("Shuffled numbers:", numbers) # Create a list of numbers from 1 to 10, shuffle it, and print the result

print()
print()
print("--------Task 4--------")
print()