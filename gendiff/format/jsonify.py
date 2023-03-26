import json


def render(diffed):
    result = {}

    def inner(data, dic):
        for item in data:
            if isinstance(item, tuple):
                key, status, value = item
                if isinstance(value, list) and status == 'changed':
                    inner(value, dic)
                elif status == 'nested':
                    nested = inner(value, {})
                    dic[key] = {'nested': nested}
                elif isinstance(value, tuple) and status == 'changed':
                    dic[key] = {
                        'status': status,
                        'update': {
                            'removed': value[0],
                            'added': value[1]
                        }
                    }
                else:
                    dic[key] = {'status': status, 'value': value}
        return dic
    return json.dumps(inner(diffed, result))
