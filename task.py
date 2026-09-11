import json

def read_file (filename) :
    """
    read the file of the given name and returns its content in a dictionnary
    """
    with open (filename, "r") as f :
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            tasks = {}
            for row in f :
                id_str, status, context,description = row.strip().split(",", maxsplit=4)
                if status not in config['status'] :
                    print(f'{status} is not a status. The task with id {id_str} will be erased.')
                else:
                    tasks[int(id_str)] = (status,context, description)
    return tasks

def add_task (tasks, description, status, context) :
    """
    add a new task with it's status and description to the dictionnary of tasks given
    """
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

        if status in config['status'] :
            id = max(tasks.keys()) + 1 if tasks else 1
            tasks[id] = (status,context, description)
            print(f"Task added. Id: {id}, Status: {status}, Context :{context}, Description: {description}")

        else :
            print(f'{status} is not a status. Use one the following: {config["status"]}')
        
    return tasks

def modify_task (id, tasks, new_description, status,context) :
    """
    modify the description and status of the task with the given id in the given dictionnary of tasks
    """
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        
    if id in tasks :
        if status not in config['status'] :
            print(f'{status} is not a status. Use one the following: {config["status"]}')
        else:
            tasks[id] = (status, context,new_description)
            print(f"Task {id} modified.")
    else :
        print("ID not found.")

    return tasks

def rm_task (id, tasks) :
    """
    remove the task with the given id in the dictionnary of tasks
    """
    deleted = tasks.pop(id)
    if deleted is None:
        print("ID not found.")
    else:
        print(f"Task {id} removed: {deleted}")

    return tasks

def show_task(tasks) :
    """
    print the list of tasks into a table
    """
    print('List of tasks:')
    print('+----+--------+---------+-------------+')
    print('| id | status | context | description |\n+----+--------+---------+-------------+')
    for t in tasks :
        print(f"| {t} | {tasks[t][0]} | {tasks[t][1]} | {tasks[t][2]} |\n+----+--------+---------+-------------+")

def save_changes (filename, tasks) :
    """
    writes the dictionnary of tasks given into the txt file
    """
    with open (filename, "w") as f :
        for id, (status,context, description) in tasks.items() :
            f.write(f"{id},{status},{context},{description}\n")


def search_task(tasks, word):
    """
    search for one string in the statuses and descriptons of the tasks dictionnary and shows the list of tasks containing the given string
    """
    filtered_tasks = {}
    for id,(status, context, description) in tasks.items() :
        if word in status or word in description or word in context :
            filtered_tasks[id]=(status, context,description)
    show_task(filtered_tasks)

def save_history(tasks,id):
    """
    writes the task with the given id in the history.txt file keeps the id the task had in the dictionnary
    """
    with open('history.txt', 'a') as f:
        status, context, description = tasks[id]
        f.write(f"{id},{status},{context},{description}\n")