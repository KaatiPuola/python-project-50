REPLACER = ' '
SPACER_COUNT = 4


def transform_to_str(value, lvl=1):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        indent = REPLACER * ((lvl * SPACER_COUNT - 2) + SPACER_COUNT)
        lines = []
        for key, inner_value in value.items():
            form_value = transform_to_str(inner_value, lvl + 1)
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
        old_value = transform_to_str(dictionary.get("old_value"), lvl)
        new_value = transform_to_str(dictionary.get("new_value"), lvl)
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
