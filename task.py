
def read_file (filename) :
    with open (filename, "r") as f :
        tasks = {}
        for row in f :
            id_str, description = row.strip().split(",",maxsplit=2)
            tasks[int(id_str)] = description
    return tasks

def add_task (tasks, description) :
    id = max(tasks.keys()) + 1 if tasks else 1
    tasks[id] = description
    print(f"Task added. Id: {id}, Description: {description}")
    return tasks

def modify_task (id, tasks, new_description) :
    if id in tasks :
        tasks[id] = new_description
        print(f"Task {id} modified.")
    else :
        print("ID not found.")

    return tasks

def rm_task (id, tasks) :
    deleted = tasks.pop(id)
    if deleted is None:
        print("ID not found.")
    else:
        print(f"Task {id} removed: {deleted}")

    return tasks

def show_task(tasks) :
    print('List of tasks:')
    print('+----+----------------+')
    print('| id | description |\n+----+----------------+')
    for t in tasks :
        print(f"| {t} | {tasks[t]} |\n+----+----------------+")

def save_changes (filename, tasks) :
    with open (filename, "w") as f :
        for id, description in tasks.items() :
            f.write(f"{id},{description}\n")

