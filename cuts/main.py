#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, sys, fileinput, re, itertools, os
from cuts import ByteCutter,CharCutter,FieldCutter

def _usage(prog_name=os.path.basename(sys.argv[0])):
    spacer = ' ' * len('usage: ')
    usage = prog_name + ' -b LIST [-S SEPARATOR] [file ...]\n' \
       + spacer + prog_name + ' -c LIST [-S SEPERATOR] [file ...]\n' \
       + spacer + prog_name \
       + ' -f LIST [-d DELIM] [-e] [-S SEPERATOR] [-s] [file ...]'

    # Return usage message with trailing whitespace removed.
    return "usage: " + usage.rstrip()

def lst(l):
    """Takes a string l and returns list split by comma

    Used to take comma delimited list from command line argument, and store
    python list when parsing via argparser.

    Example:
    >>>lst("1,2,3,4")
    [1,2,3,4]
    """
    return l.split(",")

def _parseArgs(args=sys.argv[1:]):
    """Setup argparser to process arguments and generate help"""

    # parser uses custom usage string, with 'usage: ' removed, as it is
    # added automatically via argparser.
    parser = argparse.ArgumentParser(description="Remove and/or rearrange "
                                     + "sections from each line of a file(s).",
                                     usage = _usage()[len('usage: '):])
    parser.add_argument('-b',"--bytes", action='store', type=lst, default=[],
                        help="Bytes to select")
    parser.add_argument('-c',"--chars", action='store', type=lst, default=[],
                        help="Character to select")
    parser.add_argument('-f',"--fields", action='store', type=lst, default=[],
                        help="Fields to select")
    parser.add_argument('-d',"--delimiter", action='store',default="\t",
                        help="Sets field delimiter(default is TAB)")
    parser.add_argument('-e', "--regex", action='store_true',
                        help='Enable regular expressions to be used as input '+
                              'delimiter')
    parser.add_argument('-s','--skip', action='store_true',
                        help="Skip lines that do not contain input delimiter.")
    parser.add_argument('-S', "--separator", action='store',default="\t",
                        help="Sets field separator for output.")
    parser.add_argument('file', nargs='*' ,default="-",
                        help="File(s) to cut")

    return parser.parse_args(args)

def main() :
    parsed = _parseArgs()

    # Set delim based on whether or not regex is desired by user
    delim = parsed.delimiter if parsed.regex else re.escape(parsed.delimiter)

    # Keep track of number of cutters used to allow error handling if
    # multiple options selected (only one at a time is accepted)
    num_cutters = 0

    # Read mode will be used as file read mode later. 'r' is default, changed
    # to 'rb' in the event that binary read mode is selected by user
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
        sys.stderr.write('Only one option permitted of -b, -c, -f.\n')
        sys.stderr.write(_usage() + '\n')
        sys.exit(1)

    # Check for possible specification of zero index, which is not allowed.
    # Regular expression checks for zero by itself, or in range specification
    if [n for n in positions if re.search("0:?|0$",n)]:
        sys.stderr.write('Zero is an invalid position.\n')
        sys.stderr.write(_usage() + '\n')
        sys.exit(2)

    for line in fileinput.input(parsed.file, mode = read_mode):
        if parsed.skip and not re.search(parsed.delimiter,line):
            pass
        else:
            print(cutter.cut(line))

    fileinput.close()

if __name__ == '__main__':
    main()
