#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

import csv
from vars import Var
from evaluators import ObjectEvaluator

class GlobalsList:
    def __init__(self):
        """"""
        self._globals_list = []
        self._data_list = []
        self._results_list = []

    def globals_reader(self, file_path):
        """"""
        with open(file_path, mode='r') as globals_file:
            self._globals_list = [Var(row) for row in csv.DictReader(globals_file)]

    def globals_export(self, file_path):
        """"""
        # TODO - write globals_export
        pass

    def data_reader(self, file_path):
        """"""
        with open(file_path, mode='r') as data_file:
            self._data_list = [''.join(row) for row in csv.reader(data_file)]

    def get_globals(self):
        """Return a list of the global variables"""
        return self._globals_list

    def get_data(self):
        """Return a list of the data values"""
        return self._data_list

    def get_results(self):
        """"""
        return(self._results_list)

    def merge_data(self):
        """Merge the data list with the globals list"""
        oe = ObjectEvaluator(self._data_list)

        for var in self._globals_list:
            var.value = oe.evaluate(var, var.type)
            self._results_list.append(var)

