#!/usr/bin/env python3

import os
import logging


class Logger(object):
    """ Handles Logging """

    def __init__(self, loglevel):

        self.log = logging.getLogger('hash_cli')
        self.log_level = loglevel
        self.log_path = os.path.expanduser('~')
        self.log_file = os.path.join(self.log_path, 'hash_cli.log')

        self.log = logging.getLogger('hash_cli')
        self.handler = logging.FileHandler(self.log_file)
        self.handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        )
        self.log.addHandler(self.handler)

        if self.log_level.lower() == "debug":
            self.log.setLevel(logging.DEBUG)

        elif self.log_level.lower() == "error":
            self.log.setLevel(logging.ERROR)

        else:
            self.log.setLevel(logging.INFO)
