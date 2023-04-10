import json

STATUS = {'unchanged': '    ',
          'removed': '  - ',
          'added': '  + ',
          'nested': '    '}

INDENT = '    '


def stringify(value, step=0):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        data = json.dumps(value, indent=4, separators=('', ': ')).split('\n')
        for i in range(1, len(data)):
            data[i] = INDENT * step + data[i]
        return '\n'.join(data).replace('"', '')
    else:
        return value


def render(diffed):

    def inner(data, depth=0):
        off = depth * INDENT
        next = depth + 1
        result = ['{']

        for item in data:
            key, status, val = item
            sign = STATUS.get(status)

            if status in ('added', 'removed'):
                result.append(f'{off}{sign}{key}: {stringify(val, next)}')

            elif status == 'changed':
                result.append(f'{off}{STATUS["removed"]}{key}: '
                              f'{stringify(val[0], next)}')
                result.append(f'{off}{STATUS["added"]}{key}: '
                              f'{stringify(val[1], next)}')

            elif status == 'unchanged':
                result.append(f'{off}{sign}{key}: {stringify(val)}')

            elif status == 'nested':
                result.append(f'{off}{sign}{key}: {inner(val, next)}')

        result.append(f'{off}}}')
        return '\n'.join(result)
    return inner(diffed)
