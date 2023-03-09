#!/usr/bin/python3
import argparse
from gendiff.operations import generate_diff, versioning
from gendiff.format import format_of_choice
import pathlib


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        usage='%(prog)s [options] <filepath1> <filepath2>')
    parser.add_argument('first_file',
                        type=pathlib.Path,
                        help=argparse.SUPPRESS)
    parser.add_argument('second_file',
                        type=pathlib.Path,
                        help=argparse.SUPPRESS)
    parser.add_argument('-V',
                        '--version',
                        dest='version',
                        help='output the version number',
                        action='version',
                        version=f'%(prog)s {versioning()}')
    parser.add_argument('-f',
                        '--format',
                        help='output format (default: "%(default)s")',
                        dest='form',
                        choices=['plain', 'json', 'stylish'],
                        metavar='',
                        default='stylish')
    args = parser.parse_args()
    if args.form == 'plain':
        result = generate_diff(args.first_file,
                               args.second_file,
                               format_of_choice('plain'))
    elif args.form == 'json':
        result = generate_diff(args.first_file,
                               args.second_file,
                               format_of_choice('json'))
    elif args.form == 'stylish':
        result = generate_diff(args.first_file,
                               args.second_file,
                               format_of_choice('stylish'))
    print(result)


if __name__ == "__main__":
    main()
