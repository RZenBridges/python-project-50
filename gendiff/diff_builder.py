UNCHANGED = 'unchanged'
NESTED = 'nested'
ADDED = 'added'
REMOVED = 'removed'
CHANGED = 'changed'


def build_diff(value1, value2):
    result = []

    for key in value1.keys() - value2.keys():
        result.append((key, REMOVED, value1[key]))

    for key in value2.keys() - value1.keys():
        result.append((key, ADDED, value2[key]))

    for key in value1.keys() & value2.keys():
        val1 = value1[key]
        val2 = value2[key]
        if val1 == val2:
            result.append((key, UNCHANGED, val1))
        else:
            if isinstance(val1, dict) and isinstance(val2, dict):
                result.append((key, NESTED, build_diff(val1, val2)))
            else:
                result.append((key, CHANGED, (value1[key], value2[key])))
    result.sort()
    return result
