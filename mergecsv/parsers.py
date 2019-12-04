#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

import argparse


class Parser:
    def __init__(self):
        pass

    def get_args(self):
        # Create the parser
        self._p = argparse.ArgumentParser(description='List the content of a folder',
                                          epilog='Enjoy the program! :)')

        # Add the arguments
        self._p.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

        # Execute the parse_args() method
        return self._p.parse_args()
