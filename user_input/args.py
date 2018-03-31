#!/usr/bin/env python3

import argparse

def set_input_args():
    """
    Setup Parser Args
    """
    parser = argparse.ArgumentParser(
        usage="python3 run.py --path=/tmp/file.txt",
        description="Hash all files on file sys"
    )

    parser.add_argument(
        '-p', '--path', help="absolute path of the file that will be hashed",
        required=True
    )

    return parser.parse_args()
