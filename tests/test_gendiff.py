import pytest
import os

from gendiff.gendiff import generate_diff


CONST_PATH = './tests/fixtures/'


def get_path(file_name):
    return os.path.join(CONST_PATH, file_name)


@pytest.mark.parametrize('name_file1, name_file2, formatter, expected_result',[
        ('file1.json', 'file2.json', 'stylish', 'result_json.txt'),
        ('file1.yml', 'file2.yml', 'stylish', 'result_json.txt'),
        ('nested_file1.json', 'nested_file2.json', 'stylish', 'result_nested.txt'),
        ('nested_file1.yaml', 'nested_file2.yaml', 'stylish', 'result_nested.txt'),
        ('nested_file1.json', 'nested_file2.json', 'plain', 'result_plain.txt'),
        ('nested_file1.yaml', 'nested_file2.yaml', 'plain', 'result_plain.txt')
])


def test_generate_diff(name_file1, name_file2, formatter, expected_result):
    with open(get_path(expected_result), 'r') as file:
        data_result = file.read().strip('\n')
    test_file1 = get_path(name_file1)
    test_file2 = get_path(name_file2)
    assert generate_diff(test_file1, test_file2, formatter) == data_result
