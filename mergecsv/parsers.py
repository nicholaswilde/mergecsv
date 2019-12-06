#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

import argparse


class Parser:
    def __init__(self):
        pass

    def get_args(self):
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
            "-v",
            "--verbose",
            action="store_true",
            help="print results")

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

        # Execute the parse_args() method
        return self._p.parse_args()
