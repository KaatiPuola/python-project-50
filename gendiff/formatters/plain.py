def get_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if not isinstance(value, str):
        return value
    return f"'{value}'"


def build_plain(diff, path=''):
    lines = []
    for dictionary in diff:
        old_value = get_value(dictionary.get('old_value'))
        new_value = get_value(dictionary.get('new_value'))
        new_path = f"{path}{dictionary.get('key')}"
        if dictionary['type'] == 'nested':
            lines.append(build_plain(dictionary['children'], f"{new_path}."))
        elif dictionary['type'] == 'added':
            lines.append(f"Property '{new_path}' was added with \
value: {new_value}")
        elif dictionary['type'] == 'removed':
            lines.append(f"Property '{new_path}' was removed")
        elif dictionary['type'] == 'changed':
            lines.append(f"Property '{new_path}' was updated. \
From {old_value} to {new_value}")
    result = '\n'.join(lines)
    return result
