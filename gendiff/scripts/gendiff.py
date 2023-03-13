#!/usr/bin/python3
from gendiff.operations import generate_diff
from gendiff.format import format_of_choice, CHOICES
from gendiff.cli_parsing import cli_call


def main():
    args = cli_call()
    opt_param = args.form
    if opt_param in CHOICES:
        result = generate_diff(args.first_file,
                               args.second_file,
                               format_of_choice(opt_param))
        print(result)


if __name__ == "__main__":
    main()
