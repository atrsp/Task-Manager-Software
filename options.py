import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    subparsers=parser.add_subparsers(dest='fonction')
    parser_add=subparsers.add_parser('add')
    parser_add.add_argument('commentary')
    return parser
