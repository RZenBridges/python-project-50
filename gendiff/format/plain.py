from collections import defaultdict

from gendiff.diff_builder import NESTED, ADDED, REMOVED


def stringify(value):
    if isinstance(value, (bool, int)):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif not isinstance(value, (dict, list)):
        return f"'{value}'"
    else:
        return '[complex value]'


def render(diffed):
    result = defaultdict(dict)

    def inner(data, keys):

        for item in data:
            key, status, value = item
            keys.append(key)
            path = '.'.join(keys)
            line = ''
            result[path].update({'line': line})

            if status == NESTED:
                inner(value, keys)
            elif status == ADDED:
                line = f"Property '{path}' was added with value: "\
                       f"{stringify(value)}"
                result[path].update({'line': line, status[:]: value})
            elif status == REMOVED:
                line = f"Property '{path}' was removed"
                result[path].update({'line': line, status[:]: value})

            if len(result[path]) == 3:
                line = f"Property '{path}' was updated."\
                       f" From {stringify(result[path][REMOVED])} "\
                       f"to {stringify(result[path][ADDED])}"
                result[path].update({'line': line})

            keys.pop()
        return '\n'.join([dic['line'] for dic in result.values()
                         if dic['line']])
    return inner(diffed, [])
