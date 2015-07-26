#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" bytes.py is part of cuts
This module provides the ByteCutter object.
"""
from cuts.cutter import Cutter

class ByteCutter(Cutter):
    """Cuts line into specified bytes based on input delimiter.
    Arguments:
        bts -          List that specifies which bytes to return in which order
        separator -    Output delimiter. (default '')
        no_field -     Determines output if invalid field position is specified
    """
    def __init__(self, bts, separator='', no_field=''):
        super(ByteCutter, self).__init__(bts, separator, invalid_pos=no_field)

    def line(self, line):
        """Returns line untouched, expected to be byte array.

        Argument:
            line - Input line to cut
        """
        return line
