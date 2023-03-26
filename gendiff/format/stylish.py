

OPT = {'unchanged': '    ',
       'removed': '  - ',
       'added': '  + ',
       'nested': '    '}


def conform(data):
    if data in (True, False):
        return str(data).lower()
    elif data is None:
        return 'null'
    else:
        return data


def render(diffed):

    def inner(data, depth):
        step = '    ' * depth
        depth += 1
        result = '{\n'

        if not isinstance(data, (tuple, list, dict)):
            return conform(data)

        elif isinstance(data, dict):
            for key, val in data.items():
                result += f'{step}    {key}: {inner(val, depth)}\n'

        else:
            for item in data:
                if isinstance(item, tuple):
                    key, state, val = item
                else:
                    return data

                if state == 'changed':
                    removed = inner(val[0], depth)
                    added = inner(val[1], depth)
                    result += f'{step}{OPT["removed"]}{key}: {removed}\n'
                    result += f'{step}{OPT["added"]}{key}: {added}\n'

                else:
                    result += f'{step}{OPT[state]}{key}: {inner(val, depth)}\n'

        result += step + '}'
        return result
    return inner(diffed, 0)
