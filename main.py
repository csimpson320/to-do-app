user_prompt = "Type add, show, edit, complete, or exit: "

while True:
   # Get user input and strip space chars from it
   user_action = input(user_prompt)
   user_action = user_action.strip()

   match user_action:
      case 'add':
         todo = input("Enter a todo: ") + "\n"  # Add newline char for items to be place on newline in file

         with open('todos.txt', 'r') as file:
            todos = file.readlines()

         todos.append(todo)

         with open('todos.txt', 'w') as file:
            file.writelines(todos)

      case 'show':
         # Create file object and show current todos items
         with open('todos.txt', 'r') as file:
            todos = file.readlines()

         for index, item in enumerate(todos):
            item = item.strip('\n')  # Stip newline char so it displays correctly on screen
            row = f"{index + 1}.{item.title()}"
            print(row)
      case 'edit':
         number = int(input("Number of the todo to edit: "))  # Convert user input into a int
         number = number - 1

         with open('todos.txt', 'r') as file:
            todos = file.readlines()

         new_todo = input("Enter new todo: ")
         todos[number] = new_todo + '\n'

         with open('todos.txt', 'w') as file:
            file.writelines(todos)

      case 'complete':
         number = int(input("Number of the todo to complete: "))

         with open('todos.txt', 'r') as file:
            todos = file.readlines()

         index = number - 1
         todo_to_remove = todos[index].strip('\n')
         todos.pop(index)

         with open('todos.txt', 'w') as file:
            file.writelines(todos)

         message = f"Todo {todo_to_remove} was removed from the list."
         print(message)

      case 'exit':
         break
      case _:
         print("Unknown command entered")

print('Bye!')
