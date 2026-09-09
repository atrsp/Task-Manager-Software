from option.py import create_parser
import commands.py

args = create_parser().parse_args()

try :
    with open (args.filename, 'r') as f:
        tasks = f.readlines()
    if args.fonction == 'add':
        commands.add(tasks, args.commentary, args.filename)



except FileNotFoundError:
    print('The file was not found')