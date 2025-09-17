'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
print("--------Exercise 1--------")
print()
print()

x=int(input("Enter an integer: "))
if x > 10:
    print("True")
else:
    print("False") # Checked if the inputed integer is greater than 10 and printed True if it is and False if it isn't

print()
print()
print("--------Exercise 1--------")
print()


'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
print("--------Exercise 2--------")
print()
print()
age = int(input("Enter your age: "))
student_status = input("Are you a student? (yes/no): ").strip().lower()
if age < 18 or student_status == 'yes':
    print("Ticket price is $10.")
else:
    print("Ticket price is $20.") # Checked if the user is a student or under 18 and printed the ticket price based on that

print()
print()
print("--------Exercise 2--------")
print()


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

print("--------Exercise 3--------")
print()
print()

fruits = ["apple", "banana", "orange", "grape", "mango"]
fruit_name = input("Enter a fruit name: ").strip().lower()
if fruit_name in fruits:
    print("Yes, that fruit is in the list.")
else:
    print("No, that fruit is not in the list.") # Prompted the user to enter a fruit name and checked if it was in the list of fruits and printed the appropriate message

print()
print()
print("--------Exercise 3--------")
print()


'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
print("--------Exercise 4--------")
print()
print()

year = int(input("Enter a year: ")) 
check_century = year / 100 
check_leap = year / 400
if isinstance(check_century, int) and isinstance(check_leap, int):
    print(f"{year} is a century year and a leap year.")
else:
    print(f"{year} is not a century year and a leap year.") # I tried :)

print()
print()
print("--------Exercise 4--------")
print()





#SKIPPED THIS ONE 


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
print("--------Exercise 5--------")
print()
print()

weight = int(input("Enter the order weight in kg: "))
zone = input("Enter the destination zone (A/B): ").strip().upper()
if weight < 0:
    print("Error: Order weight cannot be negative.")
elif weight == 0:
    print("error: Order weight cannot be zero.")
elif zone == 'A':
    cost = weight * 5
    print(f"Shipping cost is ${cost}.")
elif zone == 'B':
    cost = weight * 7
    print(f"Shipping cost is ${cost}.")
else:
    print("Error: Invalid destination zone.") # Calculated the shipping cost based on the weight and destination zone and printed the appropriate message
print()
print()
print("--------Exercise 5--------")
print()

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
print("--------Exercise 6--------")
print()
print()
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))
if a == b == c: 
    print("The triangle is Equilateral.")
elif a == b or b == c or a == c:
    print("The triange is Isosceles.")
elif a != b and b != c and a != c:
    print("The triangle is Scalene.") 
elif a + b <= c or a + c <= b or b + c <= a:
    print("Not a triangle.") # Determined the type of triangle based on the lengths of its sides and printed the appropriate message

print()
print()
print("--------Exercise 6--------")

