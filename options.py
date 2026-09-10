import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    subparsers=parser.add_subparsers(dest='fonction')

    parser_add=subparsers.add_parser('add')
    parser_add.add_argument('status')
    parser_add.add_argument('description')

    parser_modify=subparsers.add_parser('modify')
    parser_modify.add_argument('id',type=int)
    parser_modify.add_argument('status')
    parser_modify.add_argument('description')

    parser_modify_description=subparsers.add_parser('modify_description')
    parser_modify_description.add_argument('id',type=int)
    parser_modify_description.add_argument('description')

    parser_modify_status=subparsers.add_parser('modify_status')
    parser_modify_status.add_argument('id',type=int)
    parser_modify_status.add_argument('status')

    parser_remove=subparsers.add_parser('rm')
    parser_remove.add_argument('id',type=int)

    parser_show=subparsers.add_parser('show')

    parser_search=subparsers.add_parser('search')
    parser_search.add_argument('word')

    return parser
