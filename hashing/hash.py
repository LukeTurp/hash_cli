#!/usr/bin/env python3

import hashlib

def compute_file_hash(abs_path, logger):
    """
    Returns hash value of specified file contents.
    """
    try:
        with open(abs_path, 'rb') as fp:
            data = fp.read()
        return hashlib.sha256(data).hexdigest()

    except Exception as err:
        logger.error(
            f'[-] File hash computation resulted with error: {err} | {abs_path}'
        )
        return None
