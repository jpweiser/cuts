#!/usr/bin/env python
import re
from cuts.cutter import Cutter

class FieldCutter(Cutter) :
    def __init__(self,fields,delimiter="\t",separator="\t"):
        super(FieldCutter,self).__init__(fields,separator)
        self.delimiter = delimiter

    def cut(self,line):
        result = ''
        # Remove empty strings in case of multiple instances of delimiter
        line = [x for x in re.split(self.delimiter, line.rstrip()) if x != '']

        for i,field in enumerate(self.positions):
            try :
                index = self.setup_index(field)
                try :
                    result += line[index]
                except IndexError :
                    result += "<NONE>"
            except ValueError :
                result += field
            except TypeError:
                for j in range(int(field[0]),len(line)):
                    index = self.setup_index(j)
                    try:
                        result += line[index] + self.separator
                    except IndexError :
                        pass
                result += line[-1]
                try:
                    int(self.positions[i+1])
                    result += self.separator
                except ValueError:
                    pass

        return result
