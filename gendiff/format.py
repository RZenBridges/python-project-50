

def conform(value, check='display'):
    if value in ('True', 'False'):
        value = value.lower()
    if value == 'None':
        value = 'null'
    if value == 'display':
        return value
    if isinstance(value, dict) and check == 'dict':
        value = '[complex value]'
    return value


def jsonify(input):
    result = ''
    for i in str(input):
        if i != "'":
            result += i
        else:
            result += '"'
    return result


def stylish(input):
    """Stylises gendiff'ed dictionary into a dicionary-like output"""
    def formating(dictionary, depth):
        if not isinstance(dictionary, dict):
            return str(dictionary)
        sorted_dict = dict(
            sorted(
                dictionary.items(),
                key=lambda item: item[0][4:]
            )
        )
        result = "{\n"
        current_depth = depth
        bare_indent = "    " * current_depth
        current_depth += 1
        for key, value in sorted_dict.items():
            value = conform(value, 'display')
            result += f"{bare_indent}{key}: {formating(value, current_depth)}\n"
        result += f"{bare_indent}" + "}"
        return result
    return formating(input, 0)


def plain(input):
    """Stylises gendiff'ed dictionary into a line-by-line comparison"""
    """between two files put into gendiff command"""
    admitted = ('true', 'false', 'null', '[complex value]', '0')
    output = pre_plain(input).strip("##").split("##")
    dictionary = {}
    for item in output:
        items = item.split('--')
        value = items[1].strip('(').strip(')').split(', ')
        if dictionary.get(items[0]) is None:
            dictionary[items[0]] = {}
        if value[1].strip("'") in admitted:
            value[1] = value[1].strip("'")
        dictionary[items[0]].update({value[0].strip("'"): value[1]})
    result = ''
    for k, v in dictionary.items():
        if v.get('added') is not None and v.get('removed') is not None:
            from_ = v['removed']
            to_ = v['added']
            result += f"Property '{k}' was updated. From {from_} to {to_}\n"
        elif v.get('added') is not None:
            result += f"Property '{k}' was added with value: {v['added']}\n"
        elif v.get('removed') is not None:
            result += f"Property '{k}' was removed\n"
    return result.strip()


def pre_plain(input):
    def formating(dictionary, level):
        if not isinstance(dictionary, dict):
            return str(dictionary)
        sorted_dict = dict(
            sorted(
                dictionary.items(),
                key=lambda item: item[0][4:]
            )
        )
        path = ''
        options = ('    ', '  - ', '  + ')
        for key, value in sorted_dict.items():
            level += f"{key[4:]}."
            com = isinstance(value, dict)
            cond_1 = (not com or (com and not no_update_in_dict(value, '  - ')))
            cond_2 = (not com or (com and not no_update_in_dict(value, '  + ')))
            if key[:4] == '  - ' and cond_1:
                value = conform(value, 'dict')
                path += f"{level[:-1]}--('removed', '{value}')##"
            elif key[:4] == '  + ' and cond_2:
                value = conform(value, 'dict')
                path += f"{level[:-1]}--('added', '{value}')##"
            elif key[:4] == '    ' and not isinstance(value, dict):
                pass
            elif key[:4] in options and isinstance(value, dict):
                path += f"{formating(value, level)}"
            level = level[:-(len(key[4:]) + 1)]
        return path
    return formating(input, '')


def no_update_in_dict(dictionary, search):
    if isinstance(dictionary, dict):
        for key in dictionary:
            if search == key[:4]:
                return True
            if isinstance(dictionary[key], dict):
                return no_update_in_dict(dictionary[key], search)


def format_of_choice(arg):
    if callable(arg):
        return arg
    action = {'stylish': stylish, 'plain': plain, 'jsonify': jsonify}
    if isinstance(arg, str):
        return action[arg]
