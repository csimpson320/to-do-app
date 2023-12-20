user_prompt = "Type add, show, or exit: "

todos = []

while True:
   user_action = input(user_prompt)
   user_action = user_action.strip()

   match user_action:
      case 'add':
         todo = input("Enter a todo: ")
         todos.append(todo.capitalize())
      case 'show':
         for item in todos:
            print(item)
      case 'exit':
         break

print('Bye!')
