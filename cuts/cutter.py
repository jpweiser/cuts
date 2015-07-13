import abc, re, sys

class Cutter(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self,positions,separator):
        self.separator = separator
        self.positions = self.setup_positions(positions)


    @abc.abstractmethod
    def cut(self,line):
        """Splits line input into segments"""

    def setup_positions(self, positions):
        updated_positions = []

        for i in range(len(positions)):
            ranger = re.search('(?P<start>-?\d*):(?P<end>\d*)', positions[i])

            if ranger:

                if i > 0:
                    updated_positions.append(self.separator)
                start = self.__groupval(ranger.group('start'))
                end = self.__groupval(ranger.group('end'))

                if start and end:
                    updated_positions.append(self.__appendrange(start,end))
                elif ranger.group('start'):
                    updated_positions.append([start])
                else:
                    updated_positions.append(self.__appendrange(1,end))
            else:
                updated_positions.append(positions[i])
                try:
                    int(positions[i]), int(positions[i+1])
                    updated_positions.append(self.separator)
                except (ValueError,IndexError):
                    pass

        return updated_positions

    def setup_index(self, index):
        index = int(index)
        if index > 0 :
            index -= 1
        elif index == 0:
            # Zero indicies should not be allowed by default.
            # The index will intentionally be placed out of range,
            # forcing <NONE> to be concatenated to result
            index = sys.maxsize
        return index

    def __groupval(self,group):
        if group:
            return int(group)
        else:
            return False

    def __appendrange(self,start,end):
        range_positions = []
        for i in range(start,end):
            if i != 0:
                range_positions.append(str(i))
            if i < end - 1:
                range_positions.append(self.separator)
        return range_positions
