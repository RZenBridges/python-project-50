from gendiff.diff_builder import UNCHANGED, NESTED, ADDED, REMOVED, CHANGED

STATUS_SIGNS = {UNCHANGED: '    ',
                REMOVED: '  - ',
                ADDED: '  + ',
                NESTED: '    '}
INDENT = '    '


def stringify(value, depth=0):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        values = [
            f"{(depth + 1) * INDENT}{k}: {stringify(v, depth + 1)}"
            for k, v in value.items()
        ]
        value = '\n'.join(['{'] + values + [f'{INDENT * depth}}}'])
        return value
    else:
        return value


def render(diff):

    def inner(data, depth=0):
        off = depth * INDENT
        tail_off = off + INDENT
        result = []

        for item in data:
            key, status, val = item
            sign = STATUS_SIGNS.get(status)

            if status == NESTED:
                result.append(f'{off}{sign}{key}: '
                              f'{{\n{inner(val, depth + 1)}\n{tail_off}}}')
            elif status == CHANGED:
                result.append(f'{off}{STATUS_SIGNS[REMOVED]}{key}: '
                              f'{stringify(val[0], depth + 1)}')
                result.append(f'{off}{STATUS_SIGNS[ADDED]}{key}: '
                              f'{stringify(val[1], depth + 1)}')
            else:
                result.append(f'{off}{sign}{key}: {stringify(val, depth + 1)}')

        return '\n'.join(result)
    return f'{{\n{inner(diff)}\n}}'
