# Task Manager Software

A command-line task manager that allows you to add, modify, remove, search, and display tasks stored in a task file.
> _Auteurs: Ana Tereza RIBEIRO SOARES PEREIRA, Léandre CORDIER, Thomas JULLIERE_


## How to Use

The task manager is operated through the **Command Line Interface (CLI)**.

Each time the program is executed, it reads the task file and performs **one action**. To perform another action, you must run the program again.

The following operations are available:

### Add

Adds a new task to the task file.

You can specify the task's:

* Status (cancelled, suspended, completed, etc)
* Context (home, work, etc)
* Description ('Go to the supermarket', 'Flight to Japan', etc)

The program automatically assigns an ID to the task. The ID is the next integer after the current maximum task ID.

**Usage:**

```bash
python3 main.py task_file.json add 'status' 'context' 'description'
```

---

### Modify

Modifies all the information associated with an existing task: its status, context, and description.

The program first verifies that the specified task exists.

**Usage:**

```bash
python3 main.py task_file.json modify id 'status' 'context' 'description'
```

---

### Modify Context

Modifies **only the context** of an existing task.

The program first verifies that the specified task exists.

**Usage:**

```bash
python3 main.py task_file.json modify id 'context'
```

---

### Modify Description

Modifies **only the description** of an existing task.

The program first verifies that the specified task exists.

**Usage:**

```bash
python3 main.py task_file.json modify_description id 'description'
```

---

### Modify Status

Modifies **only the status** of an existing task.

The program first verifies that the specified task exists.

**Usage:**

```bash
python3 main.py task_file.json modify_status id 'status'
```

---

### Remove

Removes an existing task from the task file.

The program first verifies that the specified task exists.

**Usage:**

```bash
python3 main.py task_file.json rm id
```

---

### Show

Displays all tasks stored in the task file, including their IDs, statuses, contexts, and descriptions.

**Usage:**

```bash
python3 main.py task_file.json show
```

---

### Search

Searches for a string in the **status, context, and description** of all tasks and displays only the tasks in which the string appears.

**Usage:**

```bash
python3 main.py task_file.json search 'string'
```

---

## Configuration

The available task statuses can be configured through the `config.json` file.

To add a new status, open `config.json` and add the desired status to the list of allowed statuses.

The program uses this configuration in two situations:

* If a task file contains a status that is not defined in `config.json`, that status is automatically removed.
* If you attempt to create or modify a task using a status that is not defined in `config.json`, the operation will not be allowed.

---

## Data Structure

Tasks are stored in a dictionary, with each task's **ID used as the key**.

Each key is associated with a list containing the task's:

1. Status
2. Description
3. Context

This structure allows tasks to be identified and accessed through their unique IDs.

---

## CLI Parsing

The project uses Python's `argparse` library to parse command-line arguments.

`argparse` separates the different arguments provided through the command line, allowing the program to handle different commands and argument formats.

This is essential because each operation requires a different number and type of arguments. For example, the `show` command does not require a task ID, while `modify` requires an ID, a status, a context, and a description.

We also use **subparsers** to organize the different commands. Each action (`add`, `modify`, `show`, `search`, etc.) has its own subparser, which defines the arguments required for that specific operation.

---

## File Organization

The project is organized into three main Python files and one configuration file:

### `task.py`

Implements the functions responsible for managing tasks.

It contains the core operations used to add, modify, remove, search, and display tasks.

### `options.py`

Implements the command-line argument parsing using the `argparse` library.

It defines the available commands and the arguments required for each operation.

### `main.py`

The main entry point of the program.

It organizes the overall program flow and connects the command-line parser from `options.py` with the task-management functions from `task.py`.

This is the file executed from the command line.

### `config.json`

A configuration file containing the list of allowed task statuses.

It determines which statuses can be used when creating or modifying tasks and is also used to validate the statuses already present in the task file.
