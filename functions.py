def get_todos():
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos):
    with open('todos.txt', 'w') as file:
        todos1 = file.writelines(todos)
    return todos1