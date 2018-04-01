#!/usr/bin/env python3

import argparse

def set_input_args():
    """
    Setup Parser Arguments
    """
    parser = argparse.ArgumentParser(
        usage="python3 run.py --path=/tmp/foo/",
        description="Recursively hashes all files discovered within the path dir."
    )
    parser.add_argument(
        '-p', '--path', help="absolute path of the file that will be hashed.",
        required=True
    )
    parser.add_argument(
        '-o', '--outfile', help="File Name for output file.",
        required=True
    )

    return parser.parse_args()
