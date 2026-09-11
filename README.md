# Task-Manager-Software

## How to use

Our task manager works through the Command Line Interface (CLI). Each time the program is run, it reads the file that contains the tasks and executes 1 action. If you'd like to do another action, you need to run it again.
We've implemented the following features:

### Add
Adds a new Task to our tasks file. You can choose the status of the file, it's description and a context related to it. This function choses automatically an ID for the task.

How to run: 
```python
python3 name_of_code_file.py name_of_task_file.py add 'status' 'description'
```

### Modify
Verifies if the task you'd like to change exists and, if so, it modifies it's status and it's description. 

How to run: 
```python
python3 name_of_code_file.py name_of_task_file.py modify id 'status' 'description'
```

### Modify Description
Verifies if the task you'd like to change exists and, if so, it modifies ONLY it's description. 

How to run: 
```python 
python3 name_of_code_file.py name_of_task_file.py modify_description id 'description'
```

### Modify Status
Verifies if the task you'd like to change exists and, if so, it modifies ONLY it's status. 

How to run: 
```python
python3 name_of_code_file.py name_of_task_file.py modify_status id 'status'
```

### Remove
Verifies if the task you'd like to remove exists and, if so, removes it from the task file.

How to run: 
```python
python3 name_of_code_file.py name_of_task_file.py rm id
```

### Show
Lists all the tasks in the task file.

How to run: 
```python
python3 name_of_code_file.py name_of_task_file.py show
```

### Search
Searches one string through the status, the description and the context and shows only the results in which the string appears.

How to run: 
```python
python3 name_of_code_file.py name_of_task_file.py search 'string'
```

### Configuration File
It allows you to select which status are allowed to be inserted. If the task file contains any status that is not defined in the configuration file (config.json) it will automatically erase it. If you try to modify a status to a non-existing one, the program will not allow you. 

How to use: Open the file config.json and add any possible status you'd like to define in our list of status (strings).

## Basic Structure

### Data Structure

We've used a dictionary to save the tasks, using its ID's as the keys and relating the keys to a list containing the status, the description and the context.  

### How to read the CLI

We used the library argparse to divide our command line in spaces, in order to obtain each argument separately and be able to adjust to different formats of command lines. It's use was essential to the functioning of our code because each type of action the code executes requires either a different number of arguments or different type.

We used subparsers to ...
