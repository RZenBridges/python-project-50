import os
from gendiff.read_file import yaml_to_text, json_to_text


def parse_file(path):
    file_name = os.path.basename(path)
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        return yaml_to_text(path)
    if file_name.endswith('.json'):
        return json_to_text(path)
