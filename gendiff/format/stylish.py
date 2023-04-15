
STATUS = {'unchanged': '    ',
          'removed': '  - ',
          'added': '  + ',
          'nested': '    '}

INDENT = '    '


def stringify(value, off=0):
    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    elif isinstance(value, dict):

        def unfold_dict(dic, depth):
            step = INDENT * depth
            yield "{"

            for k, v in dic.items():
                new_step = INDENT * (depth + 1)
                if isinstance(v, dict):
                    unfolded = '\n'.join(unfold_dict(v, depth + 1))
                    yield f'{new_step}{k}: {unfolded}'

                else:
                    yield f'{new_step}{k}: {stringify(v)}'

            yield f"{step}}}"

        return '\n'.join(unfold_dict(value, off))

    else:
        return value


def render(diffed):

    def inner(data, depth=0):
        off = depth * INDENT
        result = ['{']

        for item in data:
            key, status, val = item
            sign = STATUS.get(status)

            if status in ('added', 'removed', 'unchanged'):
                result.append(f'{off}{sign}{key}: {stringify(val, depth + 1)}')

            elif status == 'nested':
                result.append(f'{off}{sign}{key}: {inner(val, depth + 1)}')

        result.append(f'{off}}}')
        return '\n'.join(result)
    return inner(diffed)
