#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" chars.py is part of cuts
This module provides the CharCutter object.
"""
from cuts.cutter import Cutter

class CharCutter(Cutter):
    """Cuts line into specified characters based on input delimiter.
    Arguments:
        chars -        List that specifies which chars to return in which order
        separator -    Output delimiter. (default '')
        no_field -     Determines output if invalid field position is specified
    """
    def __init__(self, chars, separator='', no_field=''):
        super(CharCutter, self).__init__(chars, separator, invalid_pos=no_field)

    def line(self, line):
        """Returns string with trailing whitespace characters removed

        Argument:
            line - Input line to cut
        """
        return line.rstrip()
