#!/usr/bin/env python3

import time

from core.args import set_input_args
from file_system.files import list_all_files
from core.logger import Logger


if __name__ == '__main__':
    log = Logger(loglevel='debug').log
    now = time.strftime('%m/%d/%YT%H:%M:%SZ')
    log.info(f'[+] hash_cli started at: {now}')

    args = set_input_args(logger=log)

    list_all_files(
        base_path=args.path,
        api_scheme=args.scheme,
        api_host=args.host,
        api_port=args.port,
        logger=log,
        version=args.api_version,
        username=args.api_user,
        password=args.api_password
    )
