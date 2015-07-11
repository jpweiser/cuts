#!/usr/bin/env python
import re
from cuts.cutter import Cutter

class FieldCutter(Cutter) :
    def __init__(self,fields,delimiter="\t",separator="\t"):
        super(FieldCutter,self).__init__(fields)
        self.delimiter = delimiter
        self.separator = separator

    def cut(self,line):

        result = ''

        # Remove empty strings in case of multiple instances of delimiter
        #line = [el for el in line.rstrip().split(self.delimiter) if el != '']
        line = [x for x in re.split(self.delimiter, line.rstrip()) if x != '']

        lineStarted = False

        for field in self.positions :
            if lineStarted :
                result += self.separator

            lineStarted = True

            try :
                index = self.setup_index(field)
                try :
                    result += line[index]
                except IndexError :
                    result += "<NONE>"
            except ValueError :
                result += field
            except TypeError:
                for i in range(int(field[0]),len(line)):
                    index = self.setup_index(i)
                    try:
                        result += line[index] + self.separator
                    except IndexError :
                        pass
                result += line[-1]

        return result
