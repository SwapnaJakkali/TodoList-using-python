import json 
todo_file = "todo_list.json"

def load_tasks():
    try:
        with open(todo_file,"r") as file:
            return json.load(file)
    except(FileNotFoundError , json.JSONDecodeError):
        return []
def save_tasks(tasks):
    with open(todo_file,"w") as file:
        json.dump(tasks,file,indent=2)

def add_tasks(task):
    tasks=load_tasks()
    tasks.append({"task":task,"done":False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No Available tasks")
    else:
        for i , task in enumerate(tasks,1):
            status = "done" if task["done"] else "Not"
            print(i,status,task['task'])
def update_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        current_status = tasks[index-1]["done"]
        tasks[index-1]["done"] = not current_status
        save_tasks(tasks)
        print(f"task {index} marjed as","complited" if tasks[index-1]['done'] else 'not complited')

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index-1)
        save_tasks(tasks)
        print("task ", removed_task['task'],"deleted successfully")
    else:
        print("invalid task number. please enter a valid number")

while True:
    print("to do list menu:")
    print("1. add task")
    print("2.view tasks")
    print("3.update task status")
    print("4.delete task")
    print("5.exit")

    choice = input("choose an option : ")

    if choice == "1":
        task = input("enter task: ")
        add_tasks(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        try:
            index = int(input("enter an index to update task : "))
            update_task(index)
        except ValueError:
            print("enter a valid number")
    elif choice == "4":
        try:
            index =int(input("enter a index to delete task : "))
            delete_task(index)
        except ValueError:
            print("enter a valid number")
    elif choice =="5":
        print("bye bye!")
        break 
    else :
        print("please choose a valid choice option..!")
