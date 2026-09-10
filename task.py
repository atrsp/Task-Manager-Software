import configuration

def read_file (filename) :
    with open (filename, "r") as f :
        tasks = {}
        for row in f :
            id_str, status, description = row.strip().split(",", maxsplit=3)
            tasks[int(id_str)] = (status, description)
    return tasks

def add_task (tasks, description, status) :
    assert status in ['started', 'suspended', 'completed','cancelled'], f'{status} is not a status'
    id = max(tasks.keys()) + 1 if tasks else 1
    tasks[id] = (status, description)
    print(f"Task added. Id: {id}, Status: {status}, Description: {description}")
    return tasks

def modify_task (id, tasks, new_description, status) :
    assert status in ['started', 'suspended', 'completed','cancelled'], f'{status} is not a status'
    if id in tasks :
        tasks[id] = (status, new_description)
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
    print('+----+--------+-------------+')
    print('| id | status | description |\n+----+--------+-------------+')
    for t in tasks :
        print(f"| {t} | {tasks[t][0]} | {tasks[t][1]} | \n+----+--------+-------------+")

def save_changes (filename, tasks) :
    with open (filename, "w") as f :
        for id, (status, description) in tasks.items() :
            f.write(f"{id},{status},{description}\n")

