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

    def inner(data, level):
        for item in data:
            if len(item) == 3:
                key, status, value = item
            else:
                key, value = item
                status = False

            level.append(key)
            lvl = '.'.join(level)

            if status == NESTED:
                inner(value, level)
            elif status == ADDED:
                line = f"Property '{lvl}' was added with value: "\
                       f"{stringify(value)}"
                listed_changes.append(line)
            elif status == REMOVED:
                line = f"Property '{lvl}' was removed"
                listed_changes.append(line)
            elif status is False:
                line = f"Property '{lvl}' was updated."\
                       f" From {stringify(value[0])} "\
                       f"to {stringify(value[1])}"
                listed_changes.append(line)

            level.pop(-1)
        return '\n'.join(listed_changes)
    return inner(diffed, [])
