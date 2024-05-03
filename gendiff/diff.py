def build_diff(file1, file2):
    diff = []
    all_keys = set(file1.keys()) | set(file2.keys())
    all_keys_sorted = sorted(all_keys)
    for key in all_keys_sorted:
        key1 = key in file1
        key2 = key in file2
        if key1 and not key2:
            diff.append({
                'type': 'removed',
                'key': key,
                'old_value': file1[key]
            })
        elif key2 and not key1:
            diff.append({
                'type': 'added',
                'key': key,
                'new_value': file2[key]
            })
        elif key1 and key2:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                child = build_diff(file1[key], file2[key])
                diff.append({
                    'type': 'nested',
                    'key': key,
                    'children': child
                })
            else:
                if file1[key] == file2[key]:
                    diff.append({
                        'type': 'unchanged',
                        'key': key,
                        'old_value': file1[key]
                    })
                else:
                    diff.append({
                        'type': 'changed',
                        'key': key,
                        'old_value': file1[key],
                        'new_value': file2[key]
                    })
    return diff
