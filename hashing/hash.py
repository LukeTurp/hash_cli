#!/usr/bin/env python3

import hashlib

def compute_file_hash(abs_path):
    """
    returning hash value of file contents
    """
    try:
        with open(abs_path, 'rb') as fp:
            data = fp.read()
        return hashlib.sha256(data).hexdigest()

    except Exception as error:
        print(
            f'[!] File hash computation resulted with error: {error} | {abs_path}'
        )
        return 'not/applicable'
