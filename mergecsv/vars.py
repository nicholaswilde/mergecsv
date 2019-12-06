#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

import re


class Var:
    def __init__(self, row):
        """"""
        if not isinstance(row, dict):
            raise TypeError(row)
        row = list(row.values())
        # Assume that the order of the rows is [Identifier, Address, Type]
        self.id = row[0]
        self.address = row[1]
        # Remove the [#] from STRING[#]
        self.type = re.search(r'([A-Z])\w+', row[2]).group()
        self.value = None

    def __repr__(self):
        """"""
        return str(self.value)

    # -----------#
    # PROPERTIES #
    # -----------#

    @property
    def index(self):
        """https://stackoverflow.com/a/11339230"""
        return int(re.search(r'\d+', self.address).group())

    @property
    def size(self):
        """"""
        if "DD" in self.address:
            s = 32
        elif "D" in self.address:
            s = 16
        else:
            s = 1
        return s

    # ----------#
    # FUNCTIONS #
    # ----------#

    def evaluate(self, evaluator):
        """"""
        evaluator.start_object(self)
