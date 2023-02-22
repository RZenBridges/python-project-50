import json
import yaml
from pathlib import PurePosixPath


def adjust_format(path):
    file_name = PurePosixPath(path).name
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        return path_to_yaml(path)
    if file_name.endswith('.json'):
        return path_to_json(path)


def path_to_yaml(file_path):
    with open(file_path) as data:
        return yaml.load(data, Loader=yaml.Loader)


def path_to_json(file_path):
    with open(file_path) as data:
        return json.load(data)
