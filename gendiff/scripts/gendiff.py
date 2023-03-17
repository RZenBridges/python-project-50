#!/usr/bin/python3
from gendiff.diff_calc import generate_diff
from gendiff.cli_parsing import cli_call


def main():
    data_1, data_2, beautify = cli_call()
    result = generate_diff(data_1, data_2, beautify)
    print(result)


if __name__ == "__main__":
    main()
