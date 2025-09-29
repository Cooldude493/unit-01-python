"""Team Assignment 4: Password Security System"""

"""Data to Collect (via input)

Username and security level requirement
Password attempts (until success or user quits)
Account lockout threshold


Rules to Code
Continue authentication attempts until success or user quits
Increase security requirements after each failed attempt
Track attempt count and implement progressive lockout warnings
Classify security breach risk (low, moderate, high, critical)


Hints & Starter Code
python
# Hint: You can't predict how many attempts a user will need
username = input("Enter username: ")
lockout_threshold = int(input("Enter lockout threshold: "))

attempts = 0
login_successful = False
# Think: What approach works when you don't know how many iterations you need?
# Your authentication logic here


Test Cases

Test 1:
Username: john_doe, Security: Medium, Lockout: 5 attempts
Attempts: "password" (fail), "123456" (fail), "secure_pass_2024" (success)
Expected: Login Success=Yes, Attempts=3, Risk Level=Low, Status=Authenticated

Test 2:
Username: admin_user, Security: High, Lockout: 3 attempts
Attempts: "admin" (fail), "password123" (fail), "admin123" (fail), "quit"
Expected: Login Success=No, Attempts=3, Risk Level=High, Status=Locked Out

Test 3:
Username: guest_user, Security: Low, Lockout: 10 attempts
Attempts: "guest" (success)
Expected: Login Success=Yes, Attempts=1, Risk Level=Low, Status=Authenticated
"""

print("--------Team Assignment 4: Password Security System--------")
print()
print()

username = input("Enter username: ")
lockout_threshold = int(input("Enter lockout threshold: "))
security_level = input("Enter security level (low, medium, high): ") #Input dictates both the password and the complexity of the password

attempts = 0
login_successful = False


while attempts < lockout_threshold:
    
    
    if security_level.lower() == "low":
        password = input("Enter password (or type 'quit' to exit): ")
        if password == "guest":
            login_successful = True
            print("Login successful!")
            break
        elif password.lower() == "quit":
            print("You have chosen to quit.")
            break
        else:
            attempts += 1
            print("Incorrect password, try again.")
            if attempts >= lockout_threshold:
                print("Account locked due to too many failed attempts.")
                break # If the user enters low security, they have to enter the password "guest" to login successfully.
    
    
    
    elif security_level.lower() == "medium":
        password = input("Enter password (or type 'quit' to exit): ")
        if password == "secure_pass_2024":
            login_successful = True
            print("Login successful!")
            break
        elif password.lower() == "quit":
            print("You have chosen to quit.")
            break
        else:
            attempts += 1
            print("Incorrect password, try again.")
            if attempts >= lockout_threshold:
                print("Account locked due to too many failed attempts.")
                break # If the user enters medium security, they have to enter the password "secure_pass_2024" to login successfully.
    
    
    
    elif security_level.lower() == "high":
        password = input("Enter password (or type 'quit' to exit): ")
        if password == "admin456":
            login_successful = True
            print("Login successful!")
            break
        elif password.lower() == "quit":
            print("You have chosen to quit.")
            break
        else:
            attempts += 1
            print("Incorrect password, try again.")
            if attempts >= lockout_threshold:
                print("Account locked due to too many failed attempts.")
                break # If the user enters high security, they have to enter the password "admin456" to login successfully.

