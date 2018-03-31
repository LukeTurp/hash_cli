#!/usr/bin/env python3
import argparse
import os
import hashlib

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

def is_valid_file(abs_path):
    """
    Checking validity of file path provided
    """
    if os.path.exists(abs_path):
        return True
    else:
        return False

def compute_file_hash(abs_path):
    """
    returning hash value of file contents
    """
    with open(abs_path, 'r') as fp:
        data = fp.read()
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    args = set_input_args()
    isFile = is_valid_file(abs_path=args.path)
    if isFile is not False:
        file_hash = compute_file_hash(abs_path=args.path)
        print(
            f'{args.path} is a valid file, and its hash value is: {file_hash}'
        )
    else:
        print(f'{args.path} is not a valid file')
