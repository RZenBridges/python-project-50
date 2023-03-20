import json
import yaml


def _read_file(file_path):
    with open(file_path) as data:
        return data.read()


def _parse_yml(data):
    return yaml.load(data, Loader=yaml.Loader)


def _parse_json(data):
    return json.loads(data)


def parse_file(path, format):
    parser = {'json': _parse_json, 'yml': _parse_yml}
    data = _read_file(path)
    format_fn = parser.get(format)
    return format_fn(data)
