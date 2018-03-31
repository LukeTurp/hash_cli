#!/usr/bin/env python3

import hashlib

def compute_file_hash(abs_path):
    """
    returning hash value of file contents
    """
    with open(abs_path, 'r') as fp:
        data = fp.read()

    return hashlib.sha256(data.encode('utf-8')).hexdigest()
