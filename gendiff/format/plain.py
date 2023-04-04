NESTED = 'nested'
CHANGED = 'changed'
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
            key, status, value = item
            level += f'{key}.'
            lvl = level[:-1]
            if status == CHANGED:
                line = f"Property '{lvl}' was updated."
                line += f" From {stringify(value[0])} "
                line += f"to {stringify(value[1])}"
                listed_changes.append(line)
            elif status == NESTED:
                inner(value, level)
            elif status == ADDED:
                line = f"Property '{lvl}' was added with value: "
                line += f"{stringify(value)}"
                listed_changes.append(line)
            elif status == REMOVED:
                line = f"Property '{lvl}' was removed"
                listed_changes.append(line)
            level = level[:-len(key) - 1]
        return '\n'.join(listed_changes)
    return inner(diffed, '')
