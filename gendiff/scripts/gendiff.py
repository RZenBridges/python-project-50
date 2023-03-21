#!/usr/bin/python3
from gendiff import generate_diff, cli


def main():
    file_1, file_2, format = cli.get_arguments()
    result = generate_diff(file_1, file_2, format)
    print(result)


if __name__ == "__main__":
    main()
