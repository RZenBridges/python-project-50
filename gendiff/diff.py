from gendiff.data_parsing import read_and_parse_file
from gendiff.format import get_format_handler


def build_diff(value1, value2):
    result = []

    for key in value1.keys() - value2.keys():
        result.append((key, 'removed', value1[key]))

    for key in value2.keys() - value1.keys():
        result.append((key, 'added', value2[key]))

    for key in value1.keys() & value2.keys():
        val1 = value1[key]
        val2 = value2[key]
        if val1 == val2:
            result.append((key, 'unchanged', val1))
        else:
            if isinstance(val1, dict) and isinstance(val2, dict):
                result.append((key, 'nested', build_diff(val1, val2)))
            else:
                result.append((key, 'changed', (value1[key], value2[key])))
    return sorted(result)


def generate_diff(file_path1, file_path2, format='stylish'):
    format_fn = get_format_handler(format)
    content1 = read_and_parse_file(file_path1)
    content2 = read_and_parse_file(file_path2)
    result = format_fn(build_diff(content1, content2))
    return result
