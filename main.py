from options import create_parser
import task

args = create_parser().parse_args()

try :
    tasks = task.read_file(args.filename)
    if args.fonction == 'add':
        tasks = task.add_task(tasks, args.description, args.status )

    elif args.fonction == 'modify':
        tasks = task.modify_task(args.id,tasks,args.description, args.status)

    elif args.fonction == 'modify_description':
        tasks = task.modify_task(args.id, tasks, args.description, tasks[args.id][0])

    elif args.fonction == 'modify_status':
        tasks = task.modify_task(args.id, tasks, tasks[args.id][1], args.status)
        

    elif args.fonction == 'rm':
        tasks = task.rm_task(args.id,tasks)

    elif args.fonction == 'show' :
        task.show_task(tasks)

    task.save_changes(args.filename, tasks)



except FileNotFoundError:
    print('The file was not found')

# filename, function, arguments = task.read_command_line ()


# if function == "add" :
#     description = arguments[0]
#     tasks = add_task (tasks, description)
    
# elif function == "modify" :
#     id = int(arguments[0])
#     description = arguments[1]
#     tasks =modify_task (id, tasks, description)

# elif function == "rm" :
#     id = int(arguments[0])
#     tasks = rm_task (id, tasks)

# elif function == "show" :
#     list_tasks (tasks)

# else :
#     print ("Function not recognized. Please use 'add', 'modify', 'rm' or 'show'.")

