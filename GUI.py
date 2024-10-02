import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],
                             [list_box, edit_button],
                           [complete_button, exit_button]],
                   font=('Helevicta', 12))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todo"])

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todos = functions.get_todos()
            todo_to_edit = values["todos"]
            new_todo = values["todo"]
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todos = functions.get_todos()
            com_todos = values["todos"]
            index = todos.index(com_todos)
            todos.pop(index)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todos'].update(value = values["todos"][0])
        case "Exit"|sg.WIN_CLOSED:
            break
window.read()
window.close()
