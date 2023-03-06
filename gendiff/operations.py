from gendiff.data_parsing import adjust_format
from gendiff.operations import stylish

def low_level_diff_1(k1, value1, value2, depth, match, minus, dif, func):
    if not isinstance(value2, str) and not isinstance(value1, str):
        main_cond = k1 in value2
        cond_1 = value1.get(k1) == value2.get(k1)
        cond_2 = not cond_1 and isinstance(value2.get(k1), dict)
        cond_3 = isinstance(value2, dict)

        if main_cond and (cond_1 or cond_2 or not cond_3):
            dif[f"{match}{k1}"] = func(value1[k1], value2[k1], depth)
        elif main_cond and not cond_1:
            dif[f"{minus}{k1}"] = func(value1[k1], value2[k1], depth)
        elif not main_cond:
            dif[f"{minus}{k1}"] = func(value1[k1], value1[k1], depth)
    else:
        dif[f"{match}{k1}"] = func(value1[k1], value1[k1], depth)
    return


def low_level_diff_2(k2, value1, value2, depth, plus, dif, func):
    main_cond = k2 in value1
    if not isinstance(value2, str) and not isinstance(value1, str):
        cond_1 = k2 in [i[:4] for i in dif.keys()]
        cond_2 = value1.get(k2) != value2.get(k2)
        cond_3 = isinstance(value2.get(k2), dict)
        term_1 = not main_cond and not cond_1
        term_2 = main_cond and cond_2 and not cond_3
        if term_1 or term_2:
            dif[f"{plus}{k2}"] = func(value2[k2], value2[k2], depth)
    return


def diff_check(json1, json2):

    def matching(value1, value2, depth):
        if type(value1) == type(value2):
            if not isinstance(value1, dict):
                return str(value1)
            if not isinstance(value2, dict):
                return str(value2)
        else:
            if not isinstance(value1, dict):
                return str(value1)
        difference = {}
        current_depth = depth
        match_indent = "    "
        minus_indent = "  - "
        plus_indent = "  + "
        current_depth += 1

        for k1 in value1:
            low_level_diff_1(k1, value1, value2, current_depth,
                             match_indent, minus_indent, difference, matching)

        for k2 in value2:
            low_level_diff_2(k2, value1, value2, current_depth,
                             plus_indent, difference, matching)
        return difference
    return matching(json1, json2, 0)


def generate_diff(file_path1, file_path2, format=stylish):
    content1 = adjust_format(file_path1)
    content2 = adjust_format(file_path2)
    result = format(diff_check(content1, content2))
    return result


def versioning():
    with open('pyproject.toml', 'r') as data:
        poetry_data = data.read().split('\n')
        for i in poetry_data:
            if i.startswith('version'):
                number = i.split()[-1]
                return number.strip('"')
