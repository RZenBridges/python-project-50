from gendiff.content import parse_yml, parse_json

PARSER_OPTIONS = {'.json': parse_json,
                  '.yml': parse_yml,
                  '.yaml': parse_yml}


def parse(file_obj, format):
    format_fn = PARSER_OPTIONS.get(format)
    if format_fn is None:
        raise ValueError(f"Unavailable parser option '{format}'. "
                         f"It has to be {'/'.join(PARSER_OPTIONS.keys())}")
    return format_fn(file_obj)
