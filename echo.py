#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Jonathan Jones"


import sys
import argparse
import string


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text."
    )
    parser.add_argument(
        "text", help="text to be manipulated"
    )
    parser.add_argument(
        "-u", "--upper", help="convert text to uppercase",
        action='store_true'
    )
    parser.add_argument(
        "-l", "--lower", help="convert text to lowercase",
        action='store_true'
    )
    parser.add_argument(
        "-t", "--title", help="convert text to titlecase",
        action='store_true'
    )
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    text = ns.text
    # optional flags
    title = ns.title
    upper = ns.upper
    lower = ns.lower

    # if len(args[1]) >= 3:
    #     print("All are true")
    #     print(args)
    #     print(len(args[1]))
    if upper:
        print(text.upper())
        return text.upper()
    if lower:
        print(text.lower())
        return text.lower()
    if title:
        print(string.capwords(text))
        return string.capwords(text)
    # if text:
    #     print(text)
    #     return text


if __name__ == '__main__':
    main(sys.argv[1:])
