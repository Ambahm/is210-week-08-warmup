#!/usr/bin/env python
# -*- coding: utf-8 -*
"""This module Evaluates Truthiness/Falsiness."""


def bool_to_str(bval):
    """Function evaluating for truthiness or falsiness = Yes/No

       Arg:
           bval(booles): Parameter to be evaluated.

       Return:
            var(str): Returns 'Yes' for truthiness; 'No' for Falsiness

       Examples:
       >>> print bool_to_str(True)
        Yes

        >>> bool_to_str(['Hugo', 'Horace', 'Helen', 'Hesther'])
        'Yes'

        >>> bool_to_str('')
        'No'

    """

    if bval:
        true_or_false = 'Yes'

    else:
        true_or_false = 'No'

    return true_or_false


if __name__ == '__main__':
    print bool_to_str(True)
    print bool_to_str('')

