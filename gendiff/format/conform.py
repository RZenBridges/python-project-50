

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
