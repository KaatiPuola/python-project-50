def to_remove(key, value):
    return {
        'type': 'removed',
        'key': key,
        'old_value': value
    }


def to_add(key, value):
    return {
        'type': 'added',
        'key': key,
        'new_value': value
    }


def to_change(key, value1, value2):
    return {
        'type': 'changed',
        'key': key,
        'old_value': value1,
        'new_value': value2
    }


def to_unchanged(key, value):
    return {
        'type': 'unchanged',
        'key': key,
        'old_value': value
    }


def to_nested(key, value1, value2):
    return {
        'type': 'nested',
        'key': key,
        'children': build_diff(value1, value2)
    }


def build_diff(file1, file2):
    diff = []
    all_keys = set(file1.keys()) | set(file2.keys())
    added = set(file2.keys()) - set(file1.keys())
    removed = set(file1.keys()) - set(file2.keys())
    for key in all_keys:
        value1 = file1.get(key)
        value2 = file2.get(key)
        if key in removed:
            diff.append(to_remove(key, value1))
        elif key in added:
            diff.append(to_add(key, value2))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(to_nested(key, value1, value2))
        elif value1 == value2:
            diff.append(to_unchanged(key, value1))
        else:
            diff.append(to_change(key, value1, value2))
    sorted_diff = sorted(diff, key=lambda x: x['key'])
    return sorted_diff
