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

    def parse_log(self, line):
        """Parse a line of the log file"""
        try:
            elements = line.split()
            status_code = elements[-2]
            if status_code in self.status_codes:
                self.status_codes[status_code] += 1
            size = int(elements[-1])
            self.total_size += size
        except (IndexError, ValueError):
            pass

    def print_summary(self):
        """Print summary of HTTP status codes and total size"""
        print("Summary of HTTP status codes and total size:")
        for code in sorted(self.status_codes):
            count = self.status_codes[code]
            if count != 0:
                print(f"{code}: {count}")
        print(f"Total size: {self.total_size} bytes")

    def process_log_file(self, filename):
        """Process a log file"""
        try:
            with open(filename, 'r') as log_file:
                for line in log_file:
                    self.parse_log(line)
                    self.lines_read += 1
                    if self.lines_read % 10 == 0:
                        self.print_summary()
        except FileNotFoundError:
            print(f"Error: {filename} not found")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_parser.py <filename>")
    else:
        filename = sys.argv[1]
        log_parser = LogParser()
        log_parser.process_log_file(filename)
        log_parser.print_summary()
