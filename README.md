# cuts
## About

Utility for cutting out portions of each line of a file, and rearranging the
remaining contents as desired.

Based on the Unix utility 'cut.' The goal is to enhance the capabilities of cut to allow rearranging, negative indexing, flexible delimiting output, and proper handling of multiple instances of input
delimiters.

## Installation
    pip install cuts

## Usage

usage: cuts [-h] [-b BYTES] [-c CHARS] [-f FIELDS] [-d DELIMITER] [-e] [-s]
            [-S SEPARATOR]
            [file [file ...]]

Remove and/or rearrange sections from each line of a file(s).

positional arguments:

  file                                  File(s) to cut

optional arguments:

  -h, --help                            show this help message and exit

  -b BYTES, --bytes BYTES               Bytes to select

  -c CHARS, --chars CHARS               Character to select

  -f FIELDS, --fields FIELDS            Fields to select

  -d DELIMITER, --delimiter DELIMITER   Sets field delimiter(default is TAB)

  -e, --regex                           Enable regular expressions to be used as input delimiter

  -s, --skip                            Skip lines that do not contain input delimiter.

  -S SEPARATOR, --separator SEPARATOR   Sets field separator for output.

## List Specification

Each of the arguments -b,-c, and -f expect a list of positions as an argument.
This list should be comma delimited, and allows for negative indexing.

Additionally, the list may include ascii characters. If included, these
characters will override the output delimiter with that character.

Ranges are permitted in the list, using a colon as below

N:M    All input positions from N to M

N:     All input positions from N to end of line

:M     All input positions from beginning of line to M

Position counting starts from one.

## Files

Each line of an arbitrary number of files may be optionally cut by naming them
each after all other parameters are set. The file names should be separated by
a space.

If no files are specified, or a '-' is used, STDIN is used.

## Bytes
(-b,--bytes)=LIST

Cuts input by byte, as specified by LIST.

## Characters

Cuts input by character, as specified by LIST.

## Fields
(-f,--fields)=LIST

Cuts input into fields separated by the input delimiter.

Example:

    Input:
        echo "this is just a test" | cuts -f 1,X,3:5 -d " " -S "."
    Output:
        thisXjust.a.test

## Delimiter
(-d,--delimiter)=DELIM

Specifies input delimiter for fields option. Default is tab character ('\t').

If the option -e is set, the delimiter will accept regular expressions,
allowing for multiple delimiters.

## Separator
(-S,--separator)=SEPARATOR

Specifies output delimiter. Will be overridden by ascii character in position
list.

## See also
cut(1)

## Development notes
Project is still under development. Any questions or comments, please email
jon@jpweiser.com
