#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" fields.py is part of cuts
This module provides the FieldCutter object.

FieldCutter -     Cuts line into fields based on input delimiter
"""
import re
from cuts.cutter import Cutter

class FieldCutter(Cutter):
    """Cuts line into specified fields based on input delimiter.
    Arguments:
        fields -       List that specifies which fields to return in which order
        delim -        Input delimeter. Can be regular expression.
                       (default '\\t')
        sep -          Output delimiter. (default '\\t')
        no_field -     Determines output if invalid field position is specified
    """
    def __init__(self, fields, delim="\t", sep="\t", no_field="<NONE>"):
        super(FieldCutter, self).__init__(fields, sep, invalid_pos=no_field)
        self.delimiter = delim

    def line(self, line):
        """Returns list of strings split by input delimeter

        Argument:
        line - Input line to cut
        """
        # Remove empty strings in case of multiple instances of delimiter
        return [x for x in re.split(self.delimiter, line.rstrip()) if x != '']
