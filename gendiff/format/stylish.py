from gendiff.diff_builder import UNCHANGED, NESTED, ADDED, REMOVED

STATUS_SIGNS = {UNCHANGED: '    ',
                REMOVED: '  - ',
                ADDED: '  + ',
                NESTED: '    '}
INDENT = '    '


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    else:
        return value


def render(diffed):

    def inner(data, depth=0):
        off = depth * INDENT
        tail_off = off + INDENT
        result = []

        for item in data:
            key, status, val = item
            sign = STATUS_SIGNS.get(status)

            if status in (ADDED, REMOVED, UNCHANGED):

                if isinstance(val, dict):
                    values = []
                    for k, v in val.items():
                        values.append(
                            inner([(k, UNCHANGED, stringify(v))], depth + 1)
                        )
                    value = '\n'.join(['{'] + values + [f'{tail_off}}}'])
                else:
                    value = stringify(val)
                result.append(f'{off}{sign}{key}: {value}')

            elif status == NESTED:
                result.append(f'{off}{sign}{key}: '
                              f'{{\n{inner(val, depth + 1)}\n{tail_off}}}')

        return '\n'.join(result)
    return f'{{\n{inner(diffed)}\n}}'
