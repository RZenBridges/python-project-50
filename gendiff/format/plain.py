NESTED = 'nested'
ADDED = 'added'
REMOVED = 'removed'


def stringify(value):
    if isinstance(value, (bool, int)):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif not isinstance(value, (dict, list)):
        return f"'{value}'"
    else:
        return "[complex value]"


def render(diffed):
    listed_changes = []
    previous_key = ''
    previous_value = ''

    def inner(data, level):

        nonlocal previous_key
        nonlocal previous_value
        for item in data:
            key, status, value = item

            level.append(key)
            lvl = '.'.join(level)

            if status == NESTED:
                inner(value, level)
            elif status == ADDED and key == previous_key:
                listed_changes.pop(-1)
                line = f"Property '{lvl}' was updated."\
                       f" From {stringify(previous_value)} "\
                       f"to {stringify(value)}"
                listed_changes.append(line)

            elif status == ADDED:
                line = f"Property '{lvl}' was added with value: "\
                       f"{stringify(value)}"
                listed_changes.append(line)
            elif status == REMOVED:
                line = f"Property '{lvl}' was removed"
                listed_changes.append(line)
                previous_key = key
                previous_value = value

            level.pop(-1)
        return '\n'.join(listed_changes)
    return inner(diffed, [])
