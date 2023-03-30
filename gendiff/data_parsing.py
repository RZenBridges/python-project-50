import os

from gendiff.content import parse
from gendiff.files import read_file


def read_and_parse_file(path):
    extension = os.path.splitext(path)[1]
    return parse(read_file(path), extension)
