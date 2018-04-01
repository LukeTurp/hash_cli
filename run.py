#!/usr/bin/env python3

from file_system.files import is_valid_file, list_all_files, delete_output_file
from user_input.args import set_input_args
from hashing.hash import compute_file_hash


if __name__ == '__main__':
    args = set_input_args()
    delete_output_file(out_file=args.outfile)
    list_all_files(base_path=args.path, out_file=args.outfile)
