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
            if status == UNCHANGED:
                continue
            keys.append(key)
            path = '.'.join(keys)

            if status == NESTED:
                inner(value, keys)
            elif status == CHANGED:
                result.append(f"Property '{path}' was updated. "
                              f"From {stringify(value[0])} "
                              f"to {stringify(value[1])}")
            elif status == ADDED:
                result.append(f"Property '{path}' was added with value: "
                              f"{stringify(value)}")
            elif status == REMOVED:
                result.append(f"Property '{path}' was removed")

            keys.pop()

        return '\n'.join([line for line in result])
    return inner(diff, [])
