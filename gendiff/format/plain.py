import json


def switch_type(data):
    if not isinstance(data, dict):
        return json.dumps(data).replace('"', "'")
    else:
        return "[complex value]"


def render(diffed):
    listed_changes = []

    def inner(data, level):
        if not isinstance(data, list):
            return

        for item in data:
            key, status, value = item
            level += f'{key}.'
            lvl = level[:-1]
            if status == 'changed':
                line = f"Property '{lvl}' was updated."
                line += f" From {switch_type(value[0])} "
                line += f"to {switch_type(value[1])}"
                listed_changes.append(line)
            elif status == 'nested' or status == 'unchanged':
                inner(value, level)
            elif status == 'added':
                line = f"Property '{lvl}' was added with value: "
                line += f"{switch_type(value)}"
                listed_changes.append(line)
            elif status == 'removed':
                line = f"Property '{lvl}' was removed"
                listed_changes.append(line)
            level = level[:-len(key) - 1]
        return '\n'.join(listed_changes)
    return inner(diffed, '')
