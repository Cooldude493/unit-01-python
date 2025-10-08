import os

import sys

"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""

print("--------Task 1--------")
print()
print()

print("Current Directory:", os.getcwd()) # Get the current working directory

print()
print()
print("--------Task 1--------")
print()


"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print("--------Task 2--------")
print()
print()

print("Contents of the current directory:", os.listdir('test_folder')) # List all files and directories in the current directory

print()
print()
print("--------Task 2--------")
print()
"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print("--------Task 3--------")
print()
print()

if not os.path.exists('data'):
    os.mkdir('data')
    print("Directory 'data' created.")
else:
    print("Directory already exists.") # Check if the directory "data" exists

print()
print()
print("--------Task 3--------")
print()




"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print("--------Task 4--------")
print()
print()

print("Contents of the current directory:", os.listdir("data"))

if os.path.isfile('data/config.txt'):
    print("File path:", os.path.abspath('data/config.txt')) # Check if the file "config.txt" exists
else:
    print("File not found.")


print()
print()
print("--------Task 4--------")
print()




"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""

print("--------Task 5--------")
print()
print()

print("Python Version:", sys.version) # Print the Python version that the user is currently using

print()
print()
print("--------Task 5--------")
print()



"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""

print("--------Task 6--------")
print()
print() 

platform = sys.platform

if platform.startswith('linux'):
    print("Platform: Linux")
elif platform == 'win32':
    print("Platform: Windows")
elif platform == 'darwin':
    print("Platform: MacOS")
else:
    print("Platform:", platform) # Print the platform the Python interpreter is running on

print()
print()
print("--------Task 6--------")
print()