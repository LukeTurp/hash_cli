#!/usr/bin/env python3

import hashlib

def compute_file_hash(abs_path, logger):
    """
    returning hash value of file contents
    """
    try:
        with open(abs_path, 'rb') as fp:
            data = fp.read()
        return hashlib.sha256(data).hexdigest()

    except Exception as error:
        logger.error(
            f'[-] File hash computation resulted with error: {error} | {abs_path}'
        )
        return None 
