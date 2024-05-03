from gendiff.parser import get_extension
from gendiff.diff import build_diff
from gendiff.stylish import build_stylish


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = get_extension(file_path1)
    file2 = get_extension(file_path2)
    diff = build_diff(file1, file2)
    return build_stylish(diff)
