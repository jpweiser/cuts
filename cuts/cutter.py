#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" cutter.py is part of cuts
This module provides the Cutter class, the base for all Cutter classes in the
cuts package.
"""

import abc, re

def group_val(group):
    """Returns value of regular expression group, if valid. 0 if not

    Argument:
        group - group to get value of
    """
    if group:
        return int(group)
    else:
        return 0

def _setup_index(index):
    """Shifts indicies as needed to account for one based indexing

    Positive indicies need to be reduced by one to match with zero based
    indexing.

    Zero is not a valid input, and as such will throw a value error.

    Arguments:
        index -     index to shift
    """
    index = int(index)
    if index > 0:
        index -= 1
    elif index == 0:
        # Zero indicies should not be allowed by default.
        raise ValueError
    return index

class Cutter(object):
    """Base class for cutters, such as FieldCutter, CharCutter, and ByteCutter

    Arguments:
        positions -    List that specifies which chars to return in which order
        separator -    Output delimiter. (default '')
        no_field -     Determines output if invalid field position is specified
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, positions, separator, invalid_pos=''):
        self.separator = separator
        self.positions = self._setup_positions(positions)
        self.invalid_pos = invalid_pos

    @abc.abstractmethod
    def line(self, line):
        """Returns prepared line for cutting"""

    def cut(self, line):
        """Returns selected positions from cut input source in desired
        arrangement.

        Argument:
            line -      input to cut
        """
        result = []
        line = self.line(line)

        for i, field in enumerate(self.positions):
            try:
                index = _setup_index(field)
                try:
                    result += line[index]
                except IndexError:
                    result.append(self.invalid_pos)
            except ValueError:
                result.append(str(field))
            except TypeError:
                result.extend(self._cut_range(line, int(field[0]), i))

        return ''.join(result)

    def _setup_positions(self, positions):
        """Processes positions to account for ranges

        Arguments:
            positions -     list of positions and/or ranges to process
        """
        updated_positions = []

        for i, position in enumerate(positions):
            ranger = re.search(r'(?P<start>-?\d*):(?P<end>\d*)', position)

            if ranger:
                if i > 0:
                    updated_positions.append(self.separator)
                start = group_val(ranger.group('start'))
                end = group_val(ranger.group('end'))

                if start and end:
                    updated_positions.extend(self._extendrange(start, end + 1))
                # Since the number of positions on a line is unknown,
                # send input to cause exception that can be caught and call
                # _cut_range helper function
                elif ranger.group('start'):
                    updated_positions.append([start])
                else:
                    updated_positions.extend(self._extendrange(1, end + 1))
            else:
                updated_positions.append(positions[i])
                try:
                    if int(position) and int(positions[i+1]):
                        updated_positions.append(self.separator)
                except (ValueError, IndexError):
                    pass

        return updated_positions


    def _cut_range(self, line, start, current_position):
        """Performs cut for range from start position to end

        Arguments:
            line -              input to cut
            start -             start of range
            current_position -  current position in main cut function
        """
        result = []
        try:
            for j in range(start, len(line)):
                index = _setup_index(j)
                try:
                    result.append(line[index])
                except IndexError:
                    result.append(self.invalid_pos)
                finally:
                    result.append(self.separator)
            result.append(line[-1])
        except IndexError:
            pass

        try:
            int(self.positions[current_position+1])
            result.append(self.separator)
        except (ValueError, IndexError):
            pass

        return result



    def _extendrange(self, start, end):
        """Creates list of values in a range with output delimiters.

        Arguments:
            start -     range start
            end -       range end
        """
        range_positions = []
        for i in range(start, end):
            if i != 0:
                range_positions.append(str(i))
            if i < end:
                range_positions.append(self.separator)
        return range_positions
