
def read_command_line () :
    

def read_file (filename) :
    with open ('test.txt', "r") as f :
        tasks = {}
        for row in f :
            id_str, description = row.strip().split(",")
            tasks[int(id_str)] = description
    return tasks

def add_task () :

def modify_task (id, tasks) :
    if id in tasks :
        
        tasks[id] = new_description
        print(f"Task {id} modified.")
    else :
        print("ID not found.")

    #change_file ()

    return tasks

def rm_task (id, tasks) :
    deleted = tasks.pop(id, None)
    if deleted is None:
        print("ID not found.")
    else:
        print(f"Task removed: {deleted}")

    return tasks

def list_tasks (tasks) :
    print('List of tasks:')
    for t in tasks :
        print(f"- Task {t}: {tasks[t]}")

def save_changes (tasks) :
    with open ('test.txt', "w") as f :
        for id, description in tasks.items() :
            f.write(f"{id},{description}\n")


filename, function, arguments = read_command_line ()
tasks = read_file (filename)

if function == "add" :
    add_task ()

elif function == "modify" :
    modify_task (arguments, tasks)

elif function == "rm" :
    rm_task (arguments, tasks)

elif function == "show" :
    list_tasks (tasks)

else :
    print ("Function not recognized. Please use 'add', 'modify', 'rm' or 'show'.")

save_changes(tasks)