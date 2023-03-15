from gendiff.format.conform import conform


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
