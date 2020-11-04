#! /usr/bin/env python3

import argparse
import os
import sys

import yaml

import re

from colorlib_gen.defs import DEFAULT_COLOR, ENGINE_COLORS

COLORS = set()

def check_file(file) -> int:
    count = 0
    pattern = re.compile(r'{([A-Za-z][\w\s]+)}')

    lines = file.readlines()
    for i, line in enumerate(lines):
        for m in pattern.finditer(line):
                if m.group(1) not in COLORS:
                    count = count + 1
                    print('{}:{}:{}: error bad color tag \'{}\''.format(file.name, i + 1, m.start(0), m.group(1)))

    return count

def parse_config(file, include_ref_colors : bool):
    """Parses ColorGen's the YAML config file."""

    cfg = yaml.load(file, Loader=yaml.Loader)

    for (key, _) in cfg['colors'].items():
            COLORS.add(key)
    
    if include_ref_colors:
        if 'ref_colors' in cfg:
            for (key, _) in cfg['ref_colors'].items():
                COLORS.add(key)

def add_default_colors():
    """Add the default engine colors."""

    for (key, _) in ENGINE_COLORS.items():
            COLORS.add(key)

def main():
    parser = argparse.ArgumentParser(
        prog='colorlib_check',
        description='ColorLib plugin and translation checker.'
        )
    parser.add_argument(
        '-e',
        '--include-engine-colors',
        action="store_true",
        dest='include_engine_colors'
        )
    parser.add_argument(
        '-r',
        '--include-ref-colors',
        action="store_true",
        dest='include_ref_colors'
        )
    parser.add_argument(
        '-c',
        '--config',
        dest='config',
        type=argparse.FileType('r', encoding='UTF-8'),
        help='config path \'{path to config dir}/color_conf.yaml\''
        )
    parser.add_argument(
        'input',
        type=argparse.FileType('r', encoding='UTF-8'),
        help='input path \'{path to include dir}/colorlib_map.inc\''
        )

    args = parser.parse_args()

    if args.config != None:
        parse_config(args.config, args.include_ref_colors)
    else:
        COLORS.add(DEFAULT_COLOR)
    
    if args.include_engine_colors or args.config is not None:
        add_default_colors()

    if check_file(args.input) > 0:
        # report an error as there were bad tags in the file
        sys.exit(1)

if __name__ == '__main__':
    main()
