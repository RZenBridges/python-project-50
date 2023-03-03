#!/usr/bin/python3
import argparse
from gendiff.operations import generate_diff
from gendiff.format import stylish, plain
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
                        help='output the version number',
                        action='version')
    parser.add_argument('-f',
                        '--format',
                        help='output format (default: "%(default)s")',
                        dest='form',
                        choices=['plain'],
                        metavar='[type]',
                        default=stylish)
    args = parser.parse_args()
    if args.form == 'plain':
        result = generate_diff(args.first_file, args.second_file, plain)
    elif args.form == stylish:
        result = generate_diff(args.first_file, args.second_file, args.form)
    print(result)


if __name__ == "__main__":
    main()
