import pytest
import os

from gendiff.gendiff import generate_diff


CONST_PATH = './tests/fixtures/'


def get_path(file_name):
    return os.path.join(CONST_PATH, file_name)


@pytest.mark.parametrize(
    'name_file1, name_file2, expected_result',
    [
        (
             'file1.json',
             'file2.json',
             'result_json.txt'
        )
    ]
)


def test_generate_diff(name_file1, name_file2, expected_result):
    with open(get_path(expected_result), 'r') as file:
        data_result = file.read()
    test_file1 = get_path(name_file1)
    test_file2 = get_path(name_file2)
    assert generate_diff(test_file1, test_file2) == data_result
