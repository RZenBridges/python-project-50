import json


def to_js(data):
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
                line += f" From {to_js(value[0])} to {to_js(value[1])}"
                listed_changes.append(line)
            elif status == 'unchanged':
                inner(value, level)
            elif status == 'added':
                line = f"Property '{lvl}' was added with value: {to_js(value)}"
                listed_changes.append(line)
            elif status == 'removed':
                line = f"Property '{lvl}' was removed"
                listed_changes.append(line)
            level = level[:-len(key) - 1]
        return '\n'.join(listed_changes)
    return inner(diffed, '')
