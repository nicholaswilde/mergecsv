#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

class IntEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        co = self._current_object
        return co.value


class ObjectEvaluator:
    def __init__(self, list):
        global data_list
        data_list = list

    def evaluate(self, evaluatable, var_type):
        """"""
        evaluator = factory.get_evaluator(var_type)
        evaluatable.evaluate(evaluator)
        return evaluator.get_value()


class EvaluatorFactory:
    def __init__(self):
        """"""
        self._creators = {}

    def register_type(self, var_type, creator):
        """"""
        self._creators[var_type] = creator

    def get_evaluator(self, var_type):
        """"""
        creator = self._creators.get(var_type)
        if not creator:
            raise ValueError(var_type)
        return creator()

factory = EvaluatorFactory()
factory.register_type("INT", IntEvaluator)
