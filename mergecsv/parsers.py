#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

import argparse


class Parser:
    def get_args(self, args=None):
        # Create the parser
        self._p = argparse.ArgumentParser(
            description="Merge exported global variable csv files from Panasonic FPWIN Pro.",
            epilog="Enjoy the program! :)")

        # Add the arguments
        self._p.add_argument(
            "globals",
            metavar="globals_path",
            type=str,
            help="the path to the global variables CSV file")

        # Add the arguments
        self._p.add_argument(
            "data",
            metavar="data_path",
            type=str,
            help="the path to the data CSV file")

        # Add the arguments
        self._p.add_argument(
            "-o",
            "--output",
            metavar="file",
            type=str,
            default="output.csv",
            help="the path to the merged output CSV file")

        # Add the arguments
        self._p.add_argument(
            "-i",
            "--id",
            metavar="NAME",
            type=str,
            help="the name of the identifier column")

        # Add the arguments
        self._p.add_argument(
            "-a",
            "--address",
            metavar="NAME",
            type=str,
            help="the name of the address column")

        # Add the arguments
        self._p.add_argument(
            "-t",
            "--type",
            metavar="NAME",
            type=str,
            help="the name of the type column")

        # Add the arguments
        self._p.add_argument(
            "-v",
            "--values",
            metavar="NAME",
            default="Values",
            type=str,
            help="the name of the values column")

        # Execute the parse_args() method
        return self._p.parse_args(args)


def _test():
    """A test method for the module"""
    p = Parser()
    args = p.get_args(["globals.csv", "data.csv"])
    print(args.globals)

if __name__ == "__main__":
    _test()
