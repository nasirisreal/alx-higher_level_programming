#!/usr/bin/python3
"""Module to parse log files and print HTTP status codes"""

import sys


class LogParser:
    """Class to parse log files and print HTTP status codes"""

    def __init__(self):
        """Initialize instance variables"""
        self.status_codes = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
        }
        self.total_size = 0
        self.lines_read = 0

    def add_status_code(self, status):
        """ add repeated number to the status code """
        if status in self.dic:
            self.dic[status] += 1

    def print_info(self, sig=0, frame=0):
        """ print status code """
        print("File size: {:d}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] != 0:
                print("{}: {:d}".format(key, self.dic[key]))


if __name__ == "__main__":
    magic = Magic()
    magic.init_dic()
    nlines = 0

    try:
        for line in sys.stdin:
            if nlines % 10 == 0 and nlines != 0:
                magic.print_info()

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                magic.add_status_code(list_line[-2])
                magic.size += int(list_line[-1].strip("\n"))
            except:
                pass
            nlines += 1
    except KeyboardInterrupt:
        magic.print_info()
        raise
    magic.print_info()
