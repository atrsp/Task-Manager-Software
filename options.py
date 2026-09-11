import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    subparsers=parser.add_subparsers(dest='fonction')

    parser_add=subparsers.add_parser('add', description= "add a new task with it's status and description to the txt file of tasks")
    parser_add.add_argument('status')
    parser_add.add_argument('context')
    parser_add.add_argument('description')

    parser_modify=subparsers.add_parser('modify', description= "modify the status and description of the task with the given id")
    parser_modify.add_argument('id',type=int)
    parser_modify.add_argument('status')
    parser_modify.add_argument('context')
    parser_modify.add_argument('description')

    parser_modify_description=subparsers.add_parser('modify_description', description= "modify the description of the task with the given id")
    parser_modify_description.add_argument('id',type=int)
    parser_modify_description.add_argument('description')

    parser_modify_status=subparsers.add_parser('modify_status', description= "modify the status of the task with the given id")
    parser_modify_status.add_argument('id',type=int)
    parser_modify_status.add_argument('status')

    parser_modify_context=subparsers.add_parser('modify_context', description= "modify the context of the task with the given id")
    parser_modify_context.add_argument('id',type=int)
    parser_modify_context.add_argument('context')

    parser_remove=subparsers.add_parser('rm', description= "remove the task with the given id")
    parser_remove.add_argument('id',type=int)

    parser_show=subparsers.add_parser('show', description="print the list of tasks in form of a table")

    parser_search=subparsers.add_parser('search',  description="shows the list of tasks containing the searched word in their status, context or description")
    parser_search.add_argument('word')

    return parser
