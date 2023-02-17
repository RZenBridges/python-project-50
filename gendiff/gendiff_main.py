#!/usr/bin/python3
import argparse
from gendiff.operations import generate_diff
import pathlib


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=pathlib.Path)
    parser.add_argument('second_file', type=pathlib.Path)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()
