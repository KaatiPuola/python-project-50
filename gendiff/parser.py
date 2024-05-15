import os
import json
import yaml


def parse(content, format_name):
    if format_name == 'json':
        return json.load(content)
    elif format_name in ['yaml', 'yml']:
        return yaml.safe_load(content)
    raise ValueError(f"Incorrect file extension: ({format_name})")


def get_content(file_path):
    _, file_extension = os.path.splitext(file_path)
    with open(file_path, 'r') as file:
        return parse(file, file_extension[1:])
