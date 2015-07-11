from cuts import Cutter

class FieldCutter(Cutter) :
    def __init__(self,fields,delimiter="\t",separator="\t"):
        self.fields = fields
        self.delimiter = delimiter
        self.separator = separator

    def cut(self,line,output=sys.stdout):

        result = ''

        line = [el for el in line.rstrip().split(self.delimiter) if el != '']
        lineNum = 0
        for field in self.fields :
            if lineNum > 0 :
                output.write(self.separator)

            lineNum += 1

            try :
                index = int(field)

                if index > 0 :
                    index -= 1
                elif index == 0 :
                    return False

                try :
                    output.write(line[index])
                except IndexError :
                    output.write("<NONE>")

            except ValueError :
                output.write(field)

        output.write("\n")
        return True
