import os

from gendiff.content.data_parsing import parse
from gendiff.diff_builder import build_diff
from gendiff.files import read_file
from gendiff.format import get_format_handler, STYLISH


def read_and_parse_file(path):
    extension = os.path.splitext(path)[1]
    return parse(read_file(path), extension)


def generate_diff(file_path1, file_path2, format=STYLISH):
    format_fn = get_format_handler(format)
    content1 = read_and_parse_file(file_path1)
    content2 = read_and_parse_file(file_path2)
    result = format_fn(build_diff(content1, content2))
    return result
