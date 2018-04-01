#!/usr/bin/env python3

import os

from hashing.hash import compute_file_hash

def delete_output_file(out_file):
    """
    Deletes output file
    """
    if os.path.exists(out_file):
        os.remove(out_file)
        return True

    else: return False

def output_hash_to_file(hash, fileName, out_file):
    """
    Write file path and it's hash to output value
    """

    with open(out_file, 'a+') as f:
        f.write(f'{fileName}, {hash}\n')


def is_valid_file(abs_path):
    """
    Checking validity of file path provided
    """
    if os.path.exists(abs_path) and os.path.isfile(abs_path) \
        and not os.path.islink(abs_path):
        return True

    else: return False


def list_all_files(base_path, out_file):
    """
    """
    for dirname, subdirList, fileList in os.walk(base_path):
         for fileName in fileList:
             file_path = os.path.join(dirname, fileName)
             isFile = is_valid_file(abs_path=file_path)

             if isFile:
                 hash = compute_file_hash(abs_path=file_path)
                 output_hash_to_file(hash=hash, fileName=file_path, out_file=out_file)
