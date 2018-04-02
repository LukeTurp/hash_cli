#!/usr/bin/env python3

import os

from hashing.hash import compute_file_hash
from clients.http import send_to_api


def is_valid_file(abs_path):
    """
    Checking validity of file path provided
    """
    if os.path.exists(abs_path) and os.path.isfile(abs_path) \
        and not os.path.islink(abs_path):
        return True

    else: return False


def list_all_files(base_path, api_scheme, api_host, api_port, logger):
    """
    Iterate over all files.  Hash and generate output
    """
    logger.info(f'[+] Starting with base_path: {base_path}')
    for dirname, subdirList, fileList in os.walk(base_path):
         for fileName in fileList:
             file_path = os.path.join(dirname, fileName)
             isFile = is_valid_file(abs_path=file_path)

             if isFile:
                 hash = compute_file_hash(abs_path=file_path, logger=logger)
                 send_to_api(
                    hash=hash,
                    abspath=file_path,
                    fileName=fileName,
                    api_scheme=api_scheme,
                    api_host=api_host,
                    api_port=api_port,
                    logger=logger
                )
