"""
For this project you are to combine your knowledge of while loops, data types, and list manipulation to create a todo tracker.

Your todo tracker should do the following:

Display the current list of todos
Allow the user to add new todo items
Allow the user to remove existing todo items
"""
todos = []

while True: # created a while loop to keep the program running until the user decides to exit
    print()
    print("Todo Tracker")
    print()
    print(todos)
    intsruction = input("Enter 'add' to add a todo, 'delete' to delete a todo, 'clear' to clear all 'exit' to quit: ").strip().lower() # User input to interact with the program
    print()
   
    if intsruction == "add":
        todo = input("Enter a new todo item: ").strip() 
        todos.append(todo)
        print()
        print(f"{todo} has been added to your todo list.")# User input to add a new todo item to the list
    
    
    elif intsruction == "delete":
        todo = int(input("Enter the number of the todo item to delete (starting from 1): ").strip())
        del todos[todo - 1]
        print()
        print(f"Todo item {todo} has been deleted.") # Allows the user to delete a specific todo item by its number in the list
        
        

    elif intsruction == "clear":
        input("Are you sure you want to clear all todo items? Type 'yes' to confirm: ").strip().lower()
        todos = []
        print()
        print("All todo items have been cleared.") # Allows the user to clear all todo items from the list

    
    
    
    
    
    
    
    
    
    elif intsruction == "exit":
        print("Exiting Todo Tracker. Goodbye!")
        break # Allows the user to exit the program

    