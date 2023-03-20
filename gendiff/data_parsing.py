import os
from gendiff import content


def read_and_parse_file(path):
    file_name = os.path.basename(path)
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        return content.parse_file(path, 'yml')
    if file_name.endswith('.json'):
        return content.parse_file(path, 'json')
