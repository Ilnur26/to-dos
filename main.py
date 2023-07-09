from modules.functions import get_todos, set_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
todos = get_todos()
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        # todo = input("Enter a todo: ") + "\n"
        todo = user_action[4:]
        todos.append(todo + "\n")

        set_todos(todos)
    elif user_action.startswith('show'):
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            # print(index, '-', item.title())
            item = item.strip('\n')
            print(f"{index + 1}-{item.title()}")
    elif user_action.startswith('edit'):
        try:
            # number = int(input("Number of todo to edit: ")) - 1
            number = int(user_action[5:]) - 1
            todos[number] = input("Enter new todo: ") + "\n"
            set_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        try:
            # number = int(input("Number of todo to delete: ")) - 1
            number = int(user_action[9:]) - 1
            # del todos[number]
            todo_to_remove = todos.pop(number).strip('\n')
            set_todos(todos)
            print(f"Todo {todo_to_remove} was removed from list")
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('exit'):
        break
    # case whatever:
    else:
        print("You entered an unknown command")

print("Bye!")
