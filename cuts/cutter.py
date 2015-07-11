import abc

class Cutter(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self,positions):
        self.positions = positions

    @abc.abstractmethod
    def cut(self,line):
        """Splits line input into segments"""
