user_prompt = "Type add, show, edit, complete, or exit: "

while True:
   # Get user input and strip space chars from it
   user_action = input(user_prompt)
   user_action = user_action.strip()

   match user_action:
      case 'add':
         todo = input("Enter a todo: ") + "\n"  # Add newline char for items to be place on newline in file

         file = open('todos.txt', 'r')
         todos = file.readlines()
         file.close()

         todos.append(todo)

         file = open('todos.txt', 'w')
         file.writelines(todos)
         file.close()
      case 'show':
         # Create file object and show current todos items
         file = open('todos.txt', 'r')
         todos = file.readlines()
         file.close()

         for index, item in enumerate(todos):
            item = item.strip('\n')  # Stip newline char so it displays correctly on screen
            row = f"{index + 1}.{item.title()}"
            print(row)
      case 'edit':
         number = int(input("Number of the todo to edit: "))
         number = number - 1
         new_todo = input("Enter new todo: ")
         todos[number] = new_todo
      case 'complete':
         number = int(input("Number of the todo to complete: "))
         todos.pop(number - 1)
      case 'exit':
         break
      case _:
         print("Unknown command entered")

print('Bye!')
