import json
import yaml

PARSER_OPTIONS = ('.json', '.yml', '.yaml')


def parse_yml(opened_file):
    return yaml.load(opened_file, Loader=yaml.Loader)


def parse_json(opened_file):
    return json.loads(opened_file)


def parser_options():
    functions = (parse_json, parse_yml, parse_yml)
    return {x: y for x, y in zip(PARSER_OPTIONS, functions)}


def parse(opened_file, format):
    format_fn = parser_options().get(format)
    if format_fn is None:
        raise ValueError(f"Unavailable parser option '{format}'. "
                         "It has to be '.json', '.yml' or '.yaml'")
    return format_fn(opened_file)
