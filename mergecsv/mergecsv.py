#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

from globalslists import GlobalsList
from parsers import Parser


def main():
    """"""
    # Get the arg parser object
    p = Parser()

    # Get the command line arguments
    args = p.get_args()

    # Get the global variables list object
    gl = GlobalsList([args.id, args.address, args.type])

    # Read the global variables CSV file
    gl.globals_reader(args.globals)

    # Read the data CSV file
    gl.data_reader(args.data)

    # Merge the data with the global variables
    gl.merge_data()

    gl.globals_writer(args.output)

if __name__ == "__main__":
    main()
