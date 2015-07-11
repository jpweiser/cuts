import abc, re, sys

class Cutter(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self,positions):
        self.positions = self.setup_positions(positions)

    @abc.abstractmethod
    def cut(self,line):
        """Splits line input into segments"""

    def setup_positions(self, positions):
        updated_positions = []

        for position in positions:
            ranger = re.search('(?P<start>-?\d*):(?P<end>\d*)', position)
            if ranger:
                if ranger.group('start') and ranger.group('end'):
                    start,end = int(ranger.group('start')), int(ranger.group('end')) + 1
                    updated_positions = range(start,end)
                elif ranger.group('start'):
                    updated_positions.append([(ranger.group('start'))])
                else:
                    updated_positions += range(1,int(ranger.group('end'))+1)

            else:
                updated_positions.append(position)

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
