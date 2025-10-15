"""
Create a program to manage a simple contact book. 
The book should store each contact's name and phone number and allow users to add, delete, and list contacts.

Extentions:
Make sure the phone number is only 10 digits
Add a check when a user attempts to edit/delete a contact that does not exist in the dictionary
Make sure a user only enters numbers not letters
"""

print("--------Contact Book--------")

contact_book = {}


while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. List Contacts")
    print("4. Exit") # Menu options for the user

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter the contacts name: ")
        pnumber = input("Enter the contacts phone number (10 digits): ")
        if pnumber.isdigit and len(pnumber) == 10:
            contact_book[name] = pnumber
            print(f"Contact {name} added.") # Adds the contact to the dictionary
        else:
            print("The phone number must be exactly 10 digits and can't contain letters.") # Checks if the phone number is valid

    elif choice == "2":
        name = input("Enter the name of the contact you would like to delete: ")
        if name in contact_book:
            del contact_book[name]
            print(f"Contact {name} deleted.") # Deletes the contact from the dictionary
        else:
            print(f"Contact {name} does not exist.") # Checks if the contact exists before attempting to delete
    
    elif choice == "3":
        if contact_book:
            print("Contacts:")
            for name, pnumber in contact_book.items(): 
                print(f"{name}: {pnumber}") # Lists all contacts in the dictionary
        else:
            print("No contacts found.") # Checks if there are any contacts to list
    
    elif choice == "4":
        print("Exiting the contact book.") # Exits the program
        break
