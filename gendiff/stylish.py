def transform_values(value):
    if isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    return value


def form_line(value, lvl=1, replacer=' ', spacer_count=4):
    value = transform_values(value)
    if isinstance(value, dict):
        indent = replacer * ((lvl * spacer_count - 2) + spacer_count)
        lines = []
        for key, inner_value in value.items():
            form_value = form_line(inner_value, lvl + 1)
            lines.append(f'{indent}  {key}: {form_value}')
        formatted_string = '\n'.join(lines)
        end_indent = lvl * spacer_count * replacer
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def build_stylish(diff, lvl=1, replacer=' ', spacer_count=4):
    lines = []
    indent = (lvl * spacer_count - 2) * replacer
    for dictionary in diff:
        key = dictionary.get("key")
        old_value = form_line(dictionary.get("old_value"), lvl)
        new_value = form_line(dictionary.get("new_value"), lvl)
        if dictionary['type'] == 'nested':
            children = build_stylish(dictionary["children"], lvl + 1)
            lines.append(f'{indent}  {key}: {children}')
        if dictionary['type'] == 'added':
            lines.append(f'{indent}+ {key}: {new_value}')
        elif dictionary['type'] == 'removed':
            lines.append(f'{indent}- {key}: {old_value}')
        elif dictionary['type'] == 'unchanged':
            lines.append(f'{indent}  {key}: {old_value}')
        elif dictionary['type'] == 'changed':
            lines.append(f'{indent}- {key}: {old_value}')
            lines.append(f'{indent}+ {key}: {new_value}')
    formatted_string = '\n'.join(lines)
    end_indent = replacer * (lvl * spacer_count - 4)
    result = f"{{\n{formatted_string}\n{end_indent}}}"
    if lvl == 1:
        result += "\n"
    return result
