#!/usr/bin/env python
# -*- coding: utf-8 -*
"""This module creates fibonacci series."""


def fibonacci(maxint):
    """Function generates a Fibonacci Number Series.
        Setting F0=0, F1=1, and then using the recursive formula
        Fn = Fn-1 + Fn-2

       Arg:
           maxint(int): Parameter for function. Setting limit for maximum limit

       Return:
            LIST(int): Returns a Fibonacci sequence listng.

       Examples:
            >>> fibonacci(5)
            [0, 1, 1, 2, 3]

            >>> fibonacci(8)
            [0, 1, 1, 2, 3, 5]

    """
    f_initial, init_plus = 0, 1             # Setting initials to 0 and 1

    fibo_list = [f_initial]                 # List starting with 0

    while init_plus < maxint:               # Fetting max limit for series loop

        f_initial, init_plus = init_plus, f_initial + init_plus
        # 0, (0+1), 1, (1+1), (2+1)

        fibo_list.append(f_initial)          # Appending numbers to list

    return fibo_list


if __name__ == '__main__':
    print fibonacci(5)
    print fibonacci(8)

