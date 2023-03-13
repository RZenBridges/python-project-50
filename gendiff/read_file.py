import json
import yaml


def yaml_to_text(file_path):
    with open(file_path) as data:
        return yaml.load(data, Loader=yaml.Loader)


def json_to_text(file_path):
    with open(file_path) as data:
        return json.load(data)
