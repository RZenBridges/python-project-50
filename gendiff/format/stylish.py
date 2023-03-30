STATUS = {'unchanged': '    ',
          'removed': '  - ',
          'added': '  + ',
          'nested': '    '}


def adjust_output(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def render(diffed):

    def inner(data, depth=0):
        if not isinstance(data, (tuple, list, dict)):
            return adjust_output(data)

        step = '    ' * depth
        depth += 1
        result = ['{']

        if isinstance(data, dict):
            for key, val in data.items():
                result.append(f'{step}    {key}: {inner(val, depth)}')

        else:
            for item in data:
                if isinstance(item, tuple):
                    key, state, val = item
                else:
                    return adjust_output(data)

                if state in STATUS:
                    value = inner(val, depth)
                    result.append(f'{step}{STATUS[state]}{key}: {value}')

                else:
                    removed = inner(val[0], depth)
                    added = inner(val[1], depth)
                    result.append(f'{step}{STATUS["removed"]}{key}: {removed}')
                    result.append(f'{step}{STATUS["added"]}{key}: {added}')

        result.append(f'{step}}}')
        return '\n'.join(result)
    return inner(diffed)
