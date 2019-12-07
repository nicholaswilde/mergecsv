#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

import csv
from collections import OrderedDict

from vars import Var
from evaluators import ObjectEvaluator


class GlobalsList:
    def __init__(self, id=None, address=None, type=None, values="Values"):
        """"""
        self._gl = [] # global variables list
        self._dl = [] # data list
        self._ol = [] # Output list
        self._hl = [id, address, type, values] # Header list

    def globals_reader(self, fp):
        """"""
        with open(fp, mode='r') as gf:
            for i, row in enumerate(csv.DictReader(gf)):
                if i == 0:
                    self._set_header(list(row.keys()))
                self._gl.append(Var(row))

    def globals_writer(self, fp):
        """"""
        with open(fp, mode='w', newline='') as gf:
            w = csv.DictWriter(gf, fieldnames=self._hl)
            w.writeheader()
            w.writerows(self._convert_to_dict())

    def data_reader(self, fp):
        """"""
        with open(fp, mode='r') as df:
            self._dl = [''.join(row) for row in csv.reader(df)]

    def get_globals(self):
        """Return a list of the global variables"""
        return self._gl

    def get_data(self):
        """Return a list of the data values"""
        return self._dl

    def get_output(self):
        """"""
        return self._ol

    def merge_data(self):
        """Merge the data list with the globals list"""
        oe = ObjectEvaluator(self._dl)
        # Loop over the global variables
        for gv in self._gl:
            # Get the global variable value
            gv.value = oe.evaluate(gv, gv.type)
            # Add it to the output list
            if gv.value != None:
                self._ol.append(gv)

    def _convert_to_dict(self):
        """"""
        l = []
        for gv in self._ol:
            l.append(OrderedDict({
                self._hl[0]: gv.id,
                self._hl[1]: gv.address,
                self._hl[2]: gv.type,
                self._hl[3]: gv.value
            }))
        return l

    def _set_header(self, l):
        """"""
        for i, key in enumerate(self._hl):
            if key == None:
                self._hl[i] = l[i]

def _test():
    """A test method for the module"""
    gl = GlobalsList(values="Values", id="Identity", address="Address", type="Type")
    gl.globals_reader('../data/globals.csv')
    gl.data_reader('../data/data.csv')
    gl.merge_data()
    print(gl._convert_to_dict())

if __name__ == "__main__":
    _test()
