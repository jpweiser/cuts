# cuts
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

Based on the Unix utility 'cut.' The goal is to enhance the capabilities of cut to allow rearranging, negative indexing, and select ranges for line numbers.

## Development notes
Development is currently focused on getting the functionality needed for the fields parameter.

One of the primary TODOs right now is to add the capability to add ranges to field selection, as well as ranges for line numbers.
