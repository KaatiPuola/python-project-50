REPLACER = ' '
SPACER_COUNT = 4


def transform_values(value):
    if isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    return value


def form_line(value, lvl=1):
    value = transform_values(value)
    if isinstance(value, dict):
        indent = REPLACER * ((lvl * SPACER_COUNT - 2) + SPACER_COUNT)
        lines = []
        for key, inner_value in value.items():
            form_value = form_line(inner_value, lvl + 1)
            lines.append(f'{indent}  {key}: {form_value}')
        formatted_string = '\n'.join(lines)
        end_indent = lvl * SPACER_COUNT * REPLACER
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def build_stylish(diff, lvl=1):
    lines = []
    indent = (lvl * SPACER_COUNT - 2) * REPLACER
    for dictionary in diff:
        key = dictionary.get("key")
        old_value = form_line(dictionary.get("old_value"), lvl)
        new_value = form_line(dictionary.get("new_value"), lvl)
        type = dictionary['type']
        match type:
            case 'nested':
                children = build_stylish(dictionary["children"], lvl + 1)
                lines.append(f'{indent}  {key}: {children}')
            case 'added':
                lines.append(f'{indent}+ {key}: {new_value}')
            case 'removed':
                lines.append(f'{indent}- {key}: {old_value}')
            case 'unchanged':
                lines.append(f'{indent}  {key}: {old_value}')
            case 'changed':
                lines.append(f'{indent}- {key}: {old_value}')
                lines.append(f'{indent}+ {key}: {new_value}')
    formatted_string = '\n'.join(lines)
    end_indent = REPLACER * (lvl * SPACER_COUNT - 4)
    return f"{{\n{formatted_string}\n{end_indent}}}"
