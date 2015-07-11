#!/usr/bin/env python

import argparse, sys, fileinput, re

def __lst(l):
    return l.split(",")

def main() :

    parser = argparse.ArgumentParser(description="Remove and/or rearrange "
        + "sections from each line of a file(s).")
    parser.add_argument('-f',"--fields", action='store', type=__lst, default=[],
        help="Fields to select")
    parser.add_argument('-d',"--delimiter", action='store',default="\t",
        help="Sets field delimiter(default is TAB)")
    parser.add_argument('-S', "--separator", action='store',default="\t",
        help="Sets field separator for output.")
    parser.add_argument('file', nargs='*' ,default="-")


    parsed = parser.parse_args(sys.argv[1:])

    cutter = FieldCutter(parsed.fields, parsed.delimiter, parsed.separator)

    for line in fileinput.input(parsed.file) :
        if not cutter.cut(line) :
            sys.stderr.write(sys.argv[0] + ": Values may not include zero.\n")
            parser.print_usage(file=sys.stderr)

    fileinput.close()

if __name__ == '__main__':
    main()
