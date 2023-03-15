from gendiff.data_parsing import parse_file
from gendiff.format import format_of_choice


def diff_check(value1, value2, nesting={}):
    # COMPLETLY REBUILT INNER DIFF STRUCTURE

    # if not isinstance(value1, dict):
    #     return value1
    # if not isinstance(value2, dict):
    #     return value2

    for item, val in value1.items():
        result = {}
        result['title'] = item
        result['changed'] = val != value2.get(item)
        term_1 = isinstance(val, dict)
        term_2 = isinstance(value2.get(item), dict)

        if result['changed'] and not term_1:
            result['removed'] = val
        elif not result['changed'] and not term_1:
            result['value'] = val

        if result['changed'] and term_1 and not term_2:
            result['removed'] = val
        elif term_2 and term_1:
            result['nested'] = diff_check(val, value2.get(item), {})

        if 'removed' in result and item in value2:
            result['added'] = value2.get(item)
        nesting.update({item: result})

    nesting.update({item: {'title': item, 'added': val}
                   for item, val in value2.items()
                   if item not in nesting})

#    for item, val in value2.items():
#        result = {}
#        result['title'] = item
#        if item not in nesting:
#            result['added'] = val
#            nesting.update({item: result})
    return nesting


def generate_diff(file_path1, file_path2, format=format_of_choice('stylish')):
    format_upd = format_of_choice(format)
    content1 = parse_file(file_path1)
    content2 = parse_file(file_path2)
    result = format_upd(diff_check(content1, content2))
    return result
