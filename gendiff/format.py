import json


def conform(value, *args):
    """Transforms boolean pythonic values and compresses dictionaries"""
    if value in (True, False):
        value = str(value).lower()
    if value is None:
        value = 'null'
    if len(args) == 0:
        return value
    if isinstance(value, dict) and args[0] == 'dict':
        value = '[complex value]'
    return value


def jsonify(diffed):
    return json.dumps(diffed)


def _priming(key, value, step, indent, cur_depth, result, form):
    #THIS FUNCTION IS USED UNSIDE STYLISH FUNCTION
    term = value.get('changed')
    if term and 'nested' in value:
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
    """Stylises gendiff'ed dictionary into a dicionary-like output"""

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
    def form(data, level):
        if not isinstance(data, dict):
            return str(data)
        sorted_data = sorted(data.keys())
        path = ''
#        flag_changed = ('removed', 'added')
        for key in sorted_data:
            value = data[key]
#            term_0 = isinstance(value, dict)
#            must = term_0 and key == value.get('title')
            title = value['title']
            level += f"{title}."
            # IN PROGRESS
        return path
    return form(diffed, '')


def no_update_in_dict(dictionary):
    if isinstance(dictionary, dict):
        for key in dictionary:
            if dictionary.get('changed') is False:
                return True
            if isinstance(dictionary.get(key), dict):
                return no_update_in_dict(dictionary[key])


def format_of_choice(arg):
    if callable(arg):
        return arg
    action = {'stylish': stylish, 'plain': plain, 'json': jsonify}
    if isinstance(arg, str):
        return action[arg]


CHOICES = ['stylish', 'plain', 'json']
