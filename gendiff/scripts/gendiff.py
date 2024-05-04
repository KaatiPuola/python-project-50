#!/usr/bin/env python3

import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        choices=['stylish', 'plain'],
        default='stylish'
    )
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    print(generate_diff(first_file, second_file, args.format))


if __name__ == '__main__':
    main()
