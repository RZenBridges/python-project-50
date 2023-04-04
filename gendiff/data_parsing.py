from gendiff.content import parse_yml, parse_json

PARSER_OPTION = {'.json': parse_json,
                 '.yml': parse_yml,
                 '.yaml': parse_yml}


def parse(opened_file, format):
    format_fn = PARSER_OPTION.get(format)
    if format_fn is None:
        raise ValueError(f"Unavailable parser option '{format}'. "
                         "It has to be '.json', '.yml' or '.yaml'")
    return format_fn(opened_file)
