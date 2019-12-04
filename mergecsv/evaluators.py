#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

from vars import Var
from words import Word

# Number of decimal places used for REAL
DEC_PLACES = 5


class StringEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        l = []
        co = self._current_object
        # Get the number of letters
        i = co.index
        # Get the length of the STRING
        n = Word(data_list[i+1]).to_int()
        # The first letter is at the 3rd word
        i += 2
        # Check if the word length is odd or even and then divide it in half
        m = n//2+1 if (n % 2) == 1 else n//2
        # Loop over the words
        for j in range(i, i+m):
            # Get the word
            w = Word(data_list[j])
            # Flip the bits
            w.value = w.flip()
            # Split the word into two 8bit pieces
            s = w.split()
            # Convert the 8bit piece to a letter
            l.append(Word(s[0]).to_string())
            l.append(Word(s[1]).to_string())
        return ''.join(l)


class RealEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        co = self._current_object
        w = Word(data_list[co.index+1] + data_list[co.index])
        return "{0:.{1}f}".format(w.to_float32(), DEC_PLACES)


class UDIntEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        co = self._current_object
        w = Word(data_list[co.index+1] + data_list[co.index])
        return w.to_int()


class UIntEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        co = self._current_object
        w = Word(data_list[co.index])
        return w.to_int()


class DIntEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        co = self._current_object
        w = Word(data_list[co.index+1] + data_list[co.index])
        return w.two_comps()


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
        w = Word(data_list[co.index])
        return w.two_comps()


class TimeEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        co = self._current_object
        w = Word(data_list[co.index+1]+data_list[co.index])
        return w.to_time()


class TimeOfDayEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        co = self._current_object
        w = Word(data_list[co.index+1]+data_list[co.index])
        return w.to_time_of_day()


class DateEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        co = self._current_object
        w = Word(data_list[co.index+1]+data_list[co.index])
        return w.to_date()


class DateAndTimeEvaluator:
    def __init__(self):
        """"""
        self._current_object = None

    def start_object(self, the_object):
        """"""
        self._current_object = the_object

    def get_value(self):
        """"""
        co = self._current_object
        w = Word(data_list[co.index+1]+data_list[co.index])
        return w.to_date_and_time()


class ObjectEvaluator:
    def __init__(self, list):
        global data_list
        data_list = list

    def evaluate(self, evaluatable, var_type):
        """"""
        evaluator = factory.get_evaluator(var_type)
        if not evaluator:
            return None
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
            return None
        return creator()


factory = EvaluatorFactory()
factory.register_type("INT", IntEvaluator)
factory.register_type("DINT", DIntEvaluator)
factory.register_type("UINT", UIntEvaluator)
factory.register_type("UDINT", UDIntEvaluator)
factory.register_type("REAL", RealEvaluator)
factory.register_type("TIME", TimeEvaluator)
factory.register_type("TIME_OF_DAY", TimeOfDayEvaluator)
factory.register_type("DATE", DateEvaluator)
factory.register_type("DATE_AND_TIME", DateAndTimeEvaluator)
factory.register_type("WORD", IntEvaluator)
factory.register_type("DWORD", DIntEvaluator)
factory.register_type("STRING", StringEvaluator)
