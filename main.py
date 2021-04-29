tasks = []

def show_tasks():
    task_index = 0
    print("\nTO-DO LIST")
    for task in tasks:
        print(f"{task} [{task_index}]")
        task_index += 1

def insert_task():
    task = input("Type the task to insert in: ")
    tasks.append(task)

def delete_task():
    try:
        task_delete_index = int(input("Insert an index of the task "
                                      "to delete: "))
    except ValueError:
        print("Index is not an integer.")
    else:
        try:
            task_delete = tasks.pop(task_delete_index)
        except IndexError:
            print("Index too big.")
        else:
            print(f"{task_delete} was deleted.")

def save_tasks():
    filename = "to_do_list.txt"
    i = 0
    with open(filename, "w") as f:
        for task in tasks:
            i += 1
            f.write(f"{i}. {task}.\n")

while True:

    print()
    print("Options:")
    print("\t0- Show tasks.")
    print("\t1- Insert the task.")
    print("\t2- Delete the task.")
    print("\t3- Save changes to the file.")
    print("\t4- Exit.")

    try:
        user_choice = int(input("Choose an option: "))
    except ValueError:
        print("Please insert an integer.")
    else:
        if user_choice == 0:
            show_tasks()
        elif user_choice == 1:
            insert_task()
        elif user_choice == 2:
            delete_task()
        elif user_choice == 3:
            save_tasks()
        elif user_choice == 4:
            break
        else:
            print("Sorry, there is no such option. Try again.")