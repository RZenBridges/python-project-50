import json


OPT = {'unchanged': '    ',
       'removed': '  - ',
       'added': '  + '}


def switch_type(data):
    if not isinstance(data, dict):
        return json.dumps(data).replace('"', "")


def render(diffed):

    def inner(data, depth):
        step = '    ' * depth
        depth += 1
        result = '{\n'

        if not isinstance(data, (tuple, list, dict)):
            return switch_type(data)

        elif isinstance(data, dict):
            for key, val in data.items():
                result += f'{step}    {key}: {inner(val, depth)}\n'

        else:
            for item in data:
                key, state, val = item
                if state == 'unchanged' or isinstance(val, dict):
                    result += f'{step}{OPT[state]}{key}: {inner(val, depth)}\n'

                elif state == 'changed':
                    removed = inner(val[0], depth)
                    added = inner(val[1], depth)
                    result += f'{step}{OPT["removed"]}{key}: {removed}\n'
                    result += f'{step}{OPT["added"]}{key}: {added}\n'

                else:
                    result += f'{step}{OPT[state]}{key}: {switch_type(val)}\n'

        result += step + '}'
        return result
    return inner(diffed, 0)
