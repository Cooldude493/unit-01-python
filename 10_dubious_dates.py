import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

print("--------Exercise 1--------")
print()
print()

now = datetime.datetime.now()
print("Current date and time:", now) # Print the current date and time

print()
print()
print("--------Exercise 1--------")
print()


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print("--------Exercise 2--------")
print()
print()

now = datetime.datetime.now()
print("Current date and time:", now) # Prints the current date and time
print()
formatted_date = now.strftime("%m/%d/%Y")
print("Formatted date (MM/DD/YYYY):", formatted_date) # Prints the formatted date

print()
print("--------Exercise 2--------")
print()

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print("--------Exercise 3--------")
print()
print()
date_string1 = "03/15/2025"
print(date_string1)
print()
date_string2 = "07/02/2025"
print(date_string2)
print()

date1 = datetime.datetime.strptime(date_string1, "%m/%d/%Y")
date2 = datetime.datetime.strptime(date_string2, "%m/%d/%Y") # Converts the strings into datetimes 

difference = date2 - date1
print(f"The difference between {date_string1} and {date_string2} is {difference.days} days.") # Prints the difference in days between the two dates

print()
print()
print("--------Exercise 3--------")
print()

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print("--------Exercise 4--------")
print()
print()

birthday_input = input("Enter your birthdate (MM/DD/YYYY): ") # Asks the user for their birthdate

birthday = datetime.datetime.strptime(birthday_input, "%m/%d/%Y") # Converts the input string into a datetime object

today = datetime.datetime.now() # Gets the current date and time

age = today - birthday # Calculates the difference between today and the user's birthday

print()
print(f"You are {age.days // 365} years old.") # Prints the user's age in years

print()
print()
print("--------Exercise 4--------")
print()

