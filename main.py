from options import create_parser
import task

args = create_parser().parse_args()

try :
    tasks = task.read_file(args.filename)
    if args.fonction == 'add':
        tasks = task.add_task(tasks, args.description, args.status,args.context)

    elif args.fonction == 'modify':
        tasks = task.modify_task(args.id,tasks,args.description, args.status,args.context)

    elif args.fonction == 'modify_description':
        tasks = task.modify_task(args.id, tasks, args.description, tasks[args.id][0],tasks[args.id][1])

    elif args.fonction == 'modify_status':
        tasks = task.modify_task(args.id, tasks, tasks[args.id][2], args.status,tasks[args.id][1])
        
    elif args.fonction == 'modify_context':
        tasks = task.modify_task(args.id, tasks, tasks[args.id][2],tasks[args.id][0],args.context)
        

    elif args.fonction == 'rm':
        tasks = task.rm_task(args.id,tasks)

    elif args.fonction == 'show' :
        task.show_task(tasks)

    elif args.fonction == 'search':
        task.search_task(tasks, args.word)

    
    task.save_changes(args.filename, tasks)



except FileNotFoundError:
    print('The file was not found')
