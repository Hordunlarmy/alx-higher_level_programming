#!/usr/bin/python3
"""
 a script that adds all arguments to a Python list,
 and then save them to a file
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_all_args(file):
    """Adds all the arguments."""
    try:
        arguments = load_from_json_file(file)
        if arguments is None:
            save_to_json_file(sys.argv[1:], file)
        else:
            arguments.extend(sys.argv[1:])
            save_to_json_file(arguments, file)
    except FileNotFoundError:
        save_to_json_file(sys.argv[1:], file)


def main():
    add_all_args("add_item.json")


if __name__ == "__main__":
    main()
