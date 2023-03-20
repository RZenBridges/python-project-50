from gendiff.diff_calc import generate_diff
from gendiff import cli


def call_gendiff():
    file_1, file_2, format = cli.get_arguments()
    result = generate_diff(file_1, file_2, format)
    print(result)
