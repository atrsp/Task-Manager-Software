import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    subparsers=parser.add_subparsers(dest='fonction')

    parser_add=subparsers.add('add')
    parser_add.add_argument('commentary')

    parser_add=subparsers.modify('modify')
    parser_add.add_argument('id')
    parser_add.add_argument('commentary')

    parser_add=subparsers.rm('rm')
    parser_add.add_argument('id')

    parser_add=subparsers.show('show')

    return parser
