import json


INDEX = {
    'removed': '  - ',
    'added': '  + ',
    'unchanged': '    '
}

CORRECT_VALUE = {
    False: 'false',
    True: 'true',
    None: 'nule'
}


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as json1:
        file1 = json.load(json1)
    with open(file_path2, 'r') as json2:
        file2 = json.load(json2)
    all_keys = set(file1.keys()) | set(file2.keys())
    all_keys_sorted = sorted(all_keys)
    diff = []
    for key in all_keys_sorted:
        key1 = key in file1
        key2 = key in file2
        if key1 and not key2:
            diff.append(('removed', key, file1[key]))
        elif key2 and not key1:
            diff.append(('added', key, file2[key]))
        elif key1 and key2:
            if file1[key] == file2[key]:
                diff.append(('unchanged', key, file1[key]))
            else:
                diff.append(('removed', key, file1[key]))
                diff.append(('added', key, file2[key]))
    result = '{\n'
    for index, key, value in diff:
        if value in CORRECT_VALUE:
            value = CORRECT_VALUE[value]
        result += f'{INDEX[index]}{key}: {value}\n'
    result += '}\n'
    return result
