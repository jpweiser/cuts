#!/usr/bin/env python
from cutter import Cutter

class FieldCutter(Cutter) :
    def __init__(self,fields,delimiter="\t",separator="\t"):
        self.fields = fields
        self.delimiter = delimiter
        self.separator = separator

    def cut(self,line):

        result = ''

        # Remove empty strings in case of multiple instances of delimiter
        line = [el for el in line.rstrip().split(self.delimiter) if el != '']

        lineStarted = False

        for field in self.fields :
            if lineStarted :
                result += self.separator

            lineStarted = True

            try :
                index = int(field)
                if index > 0 :
                    index -= 1
                elif index == 0 :
                    # Zero indicies should not be allowed.
                    # The index will intentionally be placed out of range,
                    # forcing <NONE> to be concatenated to result
                    index = len(line) + 1
                try :
                    result += line[index]
                except IndexError :
                    result += "<NONE>"

            except ValueError :
                result += field

        return result
