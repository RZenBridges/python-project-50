from gendiff.format.conform import conform


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
