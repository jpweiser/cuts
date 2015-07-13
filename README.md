# cuts
## About

Based on the Unix utility 'cut.' The goal is to enhance the capabilities of cut to allow rearranging, negative indexing, flexible delimiting output, and proper handling of multiple instances of input
delimiters.

## Installation
[Details coming soon]

## Usage

usage: cuts [-h] [-f FIELDS] [-d DELIMITER] [-S SEPARATOR] [file [file ...]]

Remove and/or rearrange sections from each line of a file(s).

positional arguments:

  file

optional arguments:

  -h, --help            show this help message and exit

  -f FIELDS, --fields FIELDS

                        Fields to select

  -d DELIMITER, --delimiter DELIMITER

                        Sets field delimiter(default is TAB)

  -S SEPARATOR, --separator SEPARATOR

                        Sets field separator for output.

## Fields
(-f,--fields)=LIST

The comma delimited list specifies the fields, which are separated by the
input delimiter.

## Delimiter
(-d,--delimiter)=DELIM

Specifies input delimiter for fields option. Accepts regular expression, allowing
for multiple delimiters. Default is tab character ('\t').

## Separator
(-S,--separator)=SEPARATOR

Specifies output delimiter.

## Development notes
Development is currently focused on getting the functionality needed for the fields parameter.
