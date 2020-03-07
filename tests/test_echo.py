#!/usr/bin/env python
# -*- coding: utf-8 -*-

import echo
import unittest
import subprocess
import string


# Your test case class goes here


class TestEcho(unittest.TestCase):

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        stdout = stdout.decode('UTF-8')
        self.assertEquals(stdout, usage)

    def test_upper(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["hello", "--upper"]
        ns = parser.parse_args(args)
        self.assertEquals(ns.upper, True)
        stdout = echo.main(args)
        usage = args[0].upper()
        self.assertEquals(stdout, usage)

    def test_lower(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["Hello", "--lower"]
        ns = parser.parse_args(args)
        self.assertEquals(ns.lower, True)
        stdout = echo.main(args)
        usage = args[0].lower()
        self.assertEquals(stdout, usage)

    def test_title(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["hello", "--title"]
        ns = parser.parse_args(args)
        self.assertEquals(ns.title, True)
        stdout = echo.main(args)
        usage = args[0].capitalize()
        self.assertEquals(stdout, usage)

    def test_all_args(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["hello", "--lower", "--upper", "--title"]
        ns = parser.parse_args(args)
        self.assertEquals(args, True)
        stdout = echo.main(args)
        usage = string.capwords(args[0]).lower().upper()
        self.assertEquals(stdout, usage)

    def test_no_args(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["Hello"]
        ns = parser.parse_args(args)
        self.assertEquals(ns.text, "Hello")
        stdout = echo.main(args)
        usage = args[0]
        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
