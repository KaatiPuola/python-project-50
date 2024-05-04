from gendiff.formatters.stylish import build_stylish
from gendiff.formatters.plain import build_plain


def get_format(diff, formatter):
    if formatter == 'stylish':
        return build_stylish(diff)
    elif formatter == 'plain':
        return build_plain(diff)
