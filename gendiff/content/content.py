import json
import yaml


def parse_yml(opened_file):
    return yaml.load(opened_file, Loader=yaml.Loader)


def parse_json(opened_file):
    return json.loads(opened_file)
