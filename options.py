import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    subparsers=parser.add_subparsers(dest='fonction')

    parser_add=subparsers.add_parser('add')
    parser_add.add_argument('state')
    parser_add.add_argument('commentary')

    parser_modify=subparsers.add_parser('modify')
    parser_modify.add_argument('id',type=int)
    parser_modify.add_argument('state')
    parser_modify.add_argument('commentary')

    parser_remove=subparsers.add_parser('rm')
    parser_remove.add_argument('id',type=int)

    parser_show=subparsers.add_parser('show')

    return parser
