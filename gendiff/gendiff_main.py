from gendiff.diff_calc import generate_diff
from gendiff.cli_parsing import cli_parse


def call_gendiff():
    data_1, data_2, beautify = cli_parse()
    result = generate_diff(data_1, data_2, beautify)
    print(result)
