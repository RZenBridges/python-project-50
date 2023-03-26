import json
import yaml


def read_file(file_path):
    with open(file_path) as data:
        return data.read()


def parse_yml(opened_file):
    return yaml.load(opened_file, Loader=yaml.Loader)


def parse_json(opened_file):
    return json.loads(opened_file)


PARSER_OPTIONS = {'json': parse_json, 'yml': parse_yml}

def parse(opened_file, format):
    format_fn = PARSER_OPTIONS.get(format)
    return format_fn(opened_file)
