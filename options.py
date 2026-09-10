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

    parser_modify_commentary=subparsers.add_parser('modify_commentary')
    parser_modify_commentary.add_argument('id',type=int)
    parser_modify_commentary.add_argument('commentary')

    parser_modify_state=subparsers.add_parser('modify_state')
    parser_modify_state.add_argument('id',type=int)
    parser_modify_state.add_argument('state')

    parser_remove=subparsers.add_parser('rm')
    parser_remove.add_argument('id',type=int)

    parser_show=subparsers.add_parser('show')

    return parser
