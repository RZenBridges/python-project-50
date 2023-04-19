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
    listed_changes = {}
    passed = {}

    def inner(data, level):

        for item in data:
            key, status, value = item
            level.append(key)
            path = '.'.join(level)

            if status == NESTED:
                inner(value, level)
            elif status == ADDED and key in passed:
                line = f"Property '{path}' was updated."\
                       f" From {stringify(passed[key])} "\
                       f"to {stringify(value)}"
                listed_changes[path] = line
            elif status == ADDED:
                line = f"Property '{path}' was added with value: "\
                       f"{stringify(value)}"
                listed_changes[path] = line
            elif status == REMOVED:
                line = f"Property '{path}' was removed"
                listed_changes[path] = line
                passed[key] = value

            level.pop(-1)
        return '\n'.join(listed_changes.values())
    return inner(diffed, [])
