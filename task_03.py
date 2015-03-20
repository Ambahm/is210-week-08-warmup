#!/usr/bin/env python
# -*- coding: utf-8 -*
"""This module counts max/min and average words per line"""

import data
import decimal

def lexicographics(to_analyze):
    """Function  to count minimum, maximum and average word per line

       Arg:
           str(str): Parameter to be evaluated.

       Return:
            tup: Returns tuple for maximum, minimum and average words.ss

       Examples:
           lexicographics('Hello how are you?'
                         '\nTesting this module'
                         '\nfor max, min and average')
            (5, 3, Decimal('4'))

            >>> lexicographics(data.SHAKESPEARE)
            (12, 5, Decimal('8.14'))

    """

    line_length = []    # Empty list to store word count per line

    # creating list for lines for line in read_file:
    read_file = to_analyze.splitlines()  # split lines
    total_line = len(read_file)

    for lines in read_file:
        line_length.append(len(lines.split()))  # word count per line

    # Methods : max(), min(), sum()

    longest_line = max(line_length)
    shortest_line = min(line_length)
    average_perline = decimal.Decimal(sum(line_length))/total_line


    return (longest_line, shortest_line, average_perline)


if __name__ == '__main__':
    print lexicographics('Hello how are you?'
                         '\nTesting this module'
                         '\nfor max, min and average')

    print lexicographics(data.SHAKESPEARE)

