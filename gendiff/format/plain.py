from gendiff.diff_builder import NESTED, ADDED, REMOVED, CHANGED, UNCHANGED


def stringify(value):
    if isinstance(value, (bool, int)):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif not isinstance(value, (dict, list)):
        return f"'{value}'"
    else:
        return '[complex value]'


def render(diff):
    result = []

    def inner(data, keys):
        for item in data:
            key, status, value = item
            keys.append(key)
            path = '.'.join(keys)
            line = None

            if status == UNCHANGED:
                keys.pop()
                continue
            elif status == NESTED:
                inner(value, keys)
            elif status == CHANGED:
                line = f"Property '{path}' was updated."\
                       f" From {stringify(value[0])} "\
                       f"to {stringify(value[1])}"
            elif status == ADDED:
                line = f"Property '{path}' was added with value: "\
                       f"{stringify(value)}"
            elif status == REMOVED:
                line = f"Property '{path}' was removed"

            keys.pop()
            result.append(line)

        return '\n'.join([line for line in result if line])
    return inner(diff, [])
