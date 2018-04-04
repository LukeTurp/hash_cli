#!/usr/bin/env python3

import os

from hashing.hash import compute_file_hash
from clients.http import HttpClient


def is_valid_file(abs_path):
    """
    Checking validity of file path provided
    """
    if os.path.exists(abs_path) and os.path.isfile(abs_path) \
        and not os.path.islink(abs_path):
        return True

    else: return False


def list_all_files(
    base_path, api_scheme, api_host, api_port, logger, version, username, password
):
    """
    Iterate over all files.  Hash and generate output
    """
    logger.info(f'[+] Starting with base_path: {base_path}')
    http_client = HttpClient(
        api_scheme=api_scheme,
        api_host=api_host,
        api_port=api_port,
        logger=logger,
        version=version,
        username=username,
        password=password
    )
    auth_success = http_client.get_jwt_token()
    if not auth_success:
        logger.error(f'[-] Failed to receive a valid hash_api token.')
        return None

    for dirname, subdirList, fileList in os.walk(base_path):
         for fileName in fileList:
             file_path = os.path.join(dirname, fileName)
             isFile = is_valid_file(abs_path=file_path)

             if isFile:
                 hash = compute_file_hash(abs_path=file_path, logger=logger)
                 http_client.send_hash_event(
                    payload={
                        'abspath': file_path,
                        'filename': fileName,
                        'hashvalue': hash
                    }
                )
    http_client.destroy_auth_token()
