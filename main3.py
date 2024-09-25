from functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete, or exit:- ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos()

    elif user_action.startswith("show"):
        todos = get_todos()

        for index,item in enumerate (todos):
            item = item.strip("\n")
            print(f"{index +1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(input("Number of the todos to edit: "))
            number =  number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos()
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(input("Number of the todo to be completed:- "))

            todos = get_todos()

            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos()

            message = f"Todo {todos_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid")

print("bye!")