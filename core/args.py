#!/usr/bin/env python3

import argparse

def set_input_args(logger):
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
        '-s', '--scheme', help="possible values: http or https.",
        required=True
    )
    parser.add_argument(
        '-a', '--host', help="host name of hash_api service.",
        required=True
    )
    parser.add_argument(
        '-d', '--port', help="network port of hash_api service.",
        required=True
    )
    args = parser.parse_args()
    logger.debug(f'[!] Received path: {args.path}')
    logger.debug(f'[!] Received scheme: {args.scheme}')
    logger.debug(f'[!] Received host: {args.host}')
    logger.debug(f'[!] Received port: {args.port}')
    return args
