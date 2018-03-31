#!/usr/bin/env python3

import os


def is_valid_file(abs_path):
    """
    Checking validity of file path provided
    """
    if os.path.exists(abs_path):
        return True
    else:
        return False
