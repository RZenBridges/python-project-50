import json


def reform(data):
    indent = {'unchanged': '    ',
              'removed': '  - ',
              'added': '  + '}
    return indent[data]


def to_js(data):
    if not isinstance(data, dict):
        return json.dumps(data).replace('"', "")


def render(diffed):

    def stylize(data, depth):
        cur_depth = depth
        step = '    ' * cur_depth
        cur_depth += 1
        result = '{\n'

        if not isinstance(data, (tuple, list, dict)):
            return to_js(data)

        elif isinstance(data, dict):
            for key, val in data.items():
                recursive = stylize(val, cur_depth)
                result += f'{step}    {key}: {recursive}\n'

        elif isinstance(data, (tuple, list)):
            for item in data:
                result, step = preform(item, step, cur_depth, stylize, result)

        result += step + '}'
        return result
    return stylize(diffed, 0)


def preform(item, step, cur_depth, stylize, result):
    key, state, val = item
    if isinstance(val, list):
        recursive = stylize(val, cur_depth)
        result += f'{step}    {key}: {recursive}\n'

    elif isinstance(val, tuple):
        recursive_A = stylize(val[0], cur_depth)
        result += f'{step}  - {key}: {recursive_A}\n'
        recursive_B = stylize(val[1], cur_depth)
        result += f'{step}  + {key}: {recursive_B}\n'

    elif not isinstance(val, dict):
        result += f'{step}{reform(state)}{key}: {to_js(val)}\n'

    elif isinstance(val, dict):
        recursive = stylize(val, cur_depth)
        result += f'{step}{reform(state)}{key}: {recursive}\n'

    return result, step
