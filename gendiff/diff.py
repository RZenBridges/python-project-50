

def build_diff(value1, value2):
    result = []

    for key in value1.keys() - value2.keys():
        result.append((key, 'removed', value1[key]))

    for key in value2.keys() - value1.keys():
        result.append((key, 'added', value2[key]))

    for key in value1.keys() & value2.keys():
        val1 = value1[key]
        val2 = value2[key]
        if val1 == val2:
            result.append((key, 'unchanged', val1))
        else:
            if isinstance(val1, dict) and isinstance(val2, dict):
                result.append((key, 'unchanged', build_diff(val1, val2)))
            else:
                result.append((key, 'changed', (value1[key], value2[key])))
    return sorted(result)
