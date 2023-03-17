import json


def reform(data):
    indent = {'unchanged': '    ', 'removed': '  - ', 'added': '  + '}
    return indent[data]


def to_js(data):
    if not isinstance(data, dict):
        return json.dumps(data).replace('"', "")


def render(diffed):

    def forme(data, depth):
        cur_depth = depth
        step = '    ' * cur_depth
        cur_depth += 1
        result = '{\n'

        if not isinstance(data, (tuple, list, dict)):
            return to_js(data)

        elif isinstance(data, dict):
            for key, val in data.items():
                recursive = forme(val, cur_depth)
                result += f'{step}    {key}: {recursive}\n'

        elif isinstance(data, (tuple, list)):
            for item in data:
                key, state, val = item
                if isinstance(val, list):
                    recursive = forme(val, cur_depth)
                    result += f'{step}    {key}: {recursive}\n'

                elif isinstance(val, tuple):
                    A = forme(val[0], cur_depth)
                    result += f'{step}  - {key}: {A}\n'
                    B = forme(val[1], cur_depth)
                    result += f'{step}  + {key}: {B}\n'

                elif not isinstance(val, dict):
                    result += f'{step}{reform(state)}{key}: {to_js(val)}\n'

                elif isinstance(val, dict):
                    recursive = forme(val, cur_depth)
                    result += f'{step}{reform(state)}{key}: {recursive}\n'

        result += step + '}'
        return result
    return forme(diffed, 0)
