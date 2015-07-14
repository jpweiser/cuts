#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, sys, fileinput, re, itertools
from cuts import ByteCutter,CharCutter,FieldCutter

def _lst(l):
    """Takes a string l and returns list split by comma"""
    return l.split(",")

def main() :

    # Setup argparser to process arguments and generate help
    parser = argparse.ArgumentParser(description="Remove and/or rearrange "
                                     + "sections from each line of a file(s).")
    parser.add_argument('-b',"--bytes", action='store', type=_lst, default=[],
                        help="Bytes to select")
    parser.add_argument('-c',"--chars", action='store', type=_lst, default=[],
                        help="Character to select")
    parser.add_argument('-f',"--fields", action='store', type=_lst, default=[],
                        help="Fields to select")
    parser.add_argument('-d',"--delimiter", action='store',default="\t",
                        help="Sets field delimiter(default is TAB)")
    parser.add_argument('-e', "--regex", action='store_true',
                        help='Enable regular expressions to be used as input'+
                              'delimiter')
    parser.add_argument('-s','--skip', action='store_true',
                        help="Skip lines that do not contain input delimiter.")
    parser.add_argument('-S', "--separator", action='store',default="\t",
                        help="Sets field separator for output.")
    parser.add_argument('file', nargs='*' ,default="-",
                        help="File(s) to cut")


    parsed = parser.parse_args(sys.argv[1:])

    # Set delim based on whether or not regex is desired by user
    delim = parsed.delimiter if parsed.regex else re.escape(parsed.delimiter)

    positions = []
    num_cutters = 0
    read_mode = 'r'

    if parsed.bytes:
        positions = parsed.bytes
        cutter = ByteCutter(positions)
        num_cutters += 1
        read_mode = 'rb'

    if parsed.chars:
        positions = parsed.chars
        cutter = CharCutter(positions)
        num_cutters += 1

    if parsed.fields:
        positions = parsed.fields
        cutter = FieldCutter(positions, delim, parsed.separator)
        num_cutters += 1

    # Make sure only one option of -b,-c, or -f is used
    if num_cutters > 1:
        print('Only one option permitted of -b, -c, -f.')
        parser.print_usage(file=sys.stderr)
        sys.exit(1)

    # Check for possible specification of zero index, which is not allowed.
    # Regular expression checks for zero by itself, or in range specification
    if list(filter(lambda position: re.search("^0:?|:0$",position), positions)):
        print('Zero is an invalid position.')
        parser.print_usage(file=sys.stderr)
        sys.exit(2)

    for line in fileinput.input(parsed.file, mode = read_mode):
        if parsed.skip and not re.search(parsed.delimiter,line):
            pass
        else:
            print(cutter.cut(line))

    fileinput.close()

if __name__ == '__main__':
    main()
