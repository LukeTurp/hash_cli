#!/usr/bin/env python3

from file_system.files import is_valid_file
from user_input.args import set_input_args
from hashing.hash import compute_file_hash


if __name__ == '__main__':
    args = set_input_args()
    isFile = is_valid_file(abs_path=args.path)

    if isFile is not False:
        file_hash = compute_file_hash(abs_path=args.path)
        print(
            f'{args.path} is a valid file, and its hash value is: {file_hash}'
        )

    else:
        print(f'{args.path} is not a valid file')
