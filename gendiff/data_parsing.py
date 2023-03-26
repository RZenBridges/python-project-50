import os
from gendiff import content


def read_and_parse_file(path):
    file_name = os.path.basename(path)
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        return content.parse(content.read_file(path), 'yml/yaml')
    if file_name.endswith('.json'):
        return content.parse(content.read_file(path), 'json')
    else:
        raise ValueError('The file has to be .json or .yml/.yaml')
