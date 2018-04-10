#!/usr/bin/env python3

import argparse

def set_input_args(logger):
    """
    Setup Parser Arguments
    """
    parser = argparse.ArgumentParser(
        usage="python3 run.py --path=/tmp/foo/ --scheme=http --host=127.0.0.1 --port=8000 \
        --api_version=1 --api_user=exampleUser --api_password=examplePassword",
        description="Recursively hashes all files discovered within the path dir."
    )
    parser.add_argument(
        '-p', '--path', help="directory from which file recursion will begin.",
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
    parser.add_argument(
        '-r', '--api_version', help="version of hash_api to run.",
        required=True
    )
    parser.add_argument(
        '-u', '--api_user', help="username for access to hash_api.",
        required=True
    )
    parser.add_argument(
        '-w', '--api_password', help="password for access to hash_api.",
        required=True
    )
    args = parser.parse_args()
    logger.debug(f'[!] Received path: {args.path}')
    logger.debug(f'[!] Received scheme: {args.scheme}')
    logger.debug(f'[!] Received host: {args.host}')
    logger.debug(f'[!] Received port: {args.port}')
    logger.debug(f'[!] Received version: {args.api_version}')
    logger.debug(f'[!] Received username: {args.api_user}')
    return args
