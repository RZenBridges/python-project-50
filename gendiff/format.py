import json


def conform(value, plained=False):
    if value in (True, False):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, str) and plained is True:
        value = f"'{value}'"
    elif isinstance(value, str) and plained is False:
        pass
    elif isinstance(value, dict):
        value = '[complex value]'
    return value


def jsonify(diffed):
    return json.dumps(diffed)


def _priming(key, value, step, indent, cur_depth, result, form):
    # THIS FUNCTION IS USED UNSIDE STYLISH FUNCTION
    term = value.get('changed')
    if term and 'nested' in value and isinstance(value['nested'], dict):
        val = conform(form(value.get('nested'), cur_depth))
        result += f"{step}{indent['bare']}{key}: {val}\n"

    elif term and 'removed' in value and 'added' in value:
        val = conform(form(value.get('removed'), cur_depth))
        result += f"{step}{indent['minus']}{key}: {val}\n"
        val = conform(form(value.get('added'), cur_depth))
        result += f"{step}{indent['plus']}{key}: {val}\n"

    elif term and 'removed' in value:
        val = conform(form(value.get('removed'), cur_depth))
        result += f"{step}{indent['minus']}{key}: {val}\n"

    elif not term and 'value' in value:
        val = conform(form(value.get('value'), cur_depth))
        result += f"{step}{indent['bare']}{key}: {val}\n"

    elif term is None:
        val = conform(form(value.get('added'), cur_depth))
        result += f"{step}{indent['plus']}{key}: {val}\n"
    return (result, step, cur_depth)


def stylish(diffed):
    """Stylizes gendiff'ed dictionary into {key: value} comparison output"""

    indent = {'bare': '    ', 'minus': '  - ', 'plus': '  + '}

    def form(data, depth):
        if not isinstance(data, dict):
            return data
        result = "{\n"
        cur_depth = depth
        step = indent['bare'] * cur_depth
        cur_depth += 1
        sorted_data = sorted(data.keys())
        for key in sorted_data:
            value = data[key]
            if isinstance(value, dict) and key == value.get('title'):
                inner = _priming(key, value, step, indent,
                                 cur_depth, result, form)
                result, step, cur_depth = inner
            else:
                val = conform(form(value, cur_depth))
                result += f"{step}{indent['bare']}{key}: {val}\n"
        result += f"{step}" + "}"
        return result
    return form(diffed, 0)


def plain(diffed):
    """ Stylizes gendiff'ed dictionary into line-by-line report on changes """
    path = []

    def form(data, level):
        sorted_data = sorted(data.keys())
        for key in sorted_data:
            value = data[key]
            title = value['title']
            level += f"{title}."
            lvl = level[:-1]
            if 'nested' in value and isinstance(value['nested'], dict):
                form(value['nested'], level)
            elif 'removed' in value and 'added' in value:
                r_val = conform(value.get('removed'), True)
                a_val = conform(value.get('added'), True)
                line = f"Property '{lvl}' was updated. From {r_val} to {a_val}"
                path.append(line)
            elif 'removed' in value and 'added' not in value:
                line = f"Property '{lvl}' was removed"
                path.append(line)
            elif 'removed' not in value and 'added' in value:
                a_val = conform(value.get('added'), True)
                line = f"Property '{lvl}' was added with value: {a_val}"
                path.append(line)
            level = level[:-len(title) - 1]
        return '\n'.join(path)
    return form(diffed, '')


def format_of_choice(arg):
    if callable(arg):
        return arg
    action = {'stylish': stylish, 'plain': plain, 'json': jsonify}
    if isinstance(arg, str):
        return action[arg]


CHOICES = ['stylish', 'plain', 'json']
