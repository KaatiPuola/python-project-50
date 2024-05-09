import os
import json
import yaml


def parse_data(file, extension):
    if extension == 'json':
        return json.load(file)
    elif extension in ['yaml', 'yml']:
        return yaml.safe_load(file)
    raise ValueError(f"Incorrect file extension: ({extension})")


def get_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    with open(file_path, 'r') as file:
        return parse_data(file, file_extension[1:])
