import json


def to_js(data):
    if not isinstance(data, dict):
        return json.dumps(data).replace('"', "'")
    else:
        return "[complex value]"


def render(diffed):
    path = []

    def inner(data, level):
        if not isinstance(data, (tuple, list, dict)):
            return data

        for item in data:
            key, status, value = item
            level += f'{key}.'
            lvl = level[:-1]
            if isinstance(value, tuple) and status == 'changed':
                A = to_js(value[0])
                B = to_js(value[1])
                line = f"Property '{lvl}' was updated. From {A} to {B}"
                path.append(line)
            elif isinstance(value, list) and status == 'unchanged':
                inner(value, level)
            elif status == 'added':
                B = to_js(value)
                line = f"Property '{lvl}' was added with value: {B}"
                path.append(line)
            elif status == 'removed':
                line = f"Property '{lvl}' was removed"
                path.append(line)
            level = level[:-len(key) - 1]
        return '\n'.join(path)
    return inner(diffed, '')
