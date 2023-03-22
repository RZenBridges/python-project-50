from gendiff.data_parsing import read_and_parse_file
from gendiff.diff import build_diff
from gendiff.format import get_format_handler


def generate_diff(file_path1, file_path2, format='stylish'):
    format_fn = get_format_handler(format)
    content1 = read_and_parse_file(file_path1)
    content2 = read_and_parse_file(file_path2)
    result = format_fn(build_diff(content1, content2))
    return result
