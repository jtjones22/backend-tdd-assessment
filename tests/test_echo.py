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

    def test_upper_long(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["hello", "--upper"]
        ns = parser.parse_args(args)
        self.assertTrue(ns.upper)
        stdout = echo.main(args)
        usage = "HELLO"
        self.assertEquals(stdout, usage)

    def test_upper_short(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["hello", "-u"]
        ns = parser.parse_args(args)
        self.assertTrue(ns.upper)
        stdout = echo.main(args)
        usage = "HELLO"
        self.assertEquals(stdout, usage)

    def test_lower_long(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["Hello", "--lower"]
        ns = parser.parse_args(args)
        self.assertTrue(ns.lower)
        stdout = echo.main(args)
        usage = "hello"
        self.assertEquals(stdout, usage)
    
    def test_lower_short(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["Hello", "-l"]
        ns = parser.parse_args(args)
        self.assertTrue(ns.lower)
        stdout = echo.main(args)
        usage = "hello"
        self.assertEquals(stdout, usage)

    def test_title_long(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["hello", "--title"]
        ns = parser.parse_args(args)
        self.assertTrue(ns.title)
        stdout = echo.main(args)
        usage = "Hello"
        self.assertEquals(stdout, usage)

    def test_title_short(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["hello", "-t"]
        ns = parser.parse_args(args)
        self.assertTrue(ns.title)
        stdout = echo.main(args)
        usage = "Hello"
        self.assertEquals(stdout, usage)

    def test_all_args(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["heLlO", "-tul"]
        ns = parser.parse_args(args)
        self.assertTrue(ns.title)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.upper)
        self.assertEquals(ns.text, "heLlO")
        stdout = echo.main(args)
        usage = "hello"
        self.assertEquals(stdout, usage)

    def test_no_args(self):
        """ Running the program without arguments should show usage. """
        parser = echo.create_parser()
        args = ["Hello"]
        ns = parser.parse_args(args)
        self.assertEquals(ns.text, "Hello")
        stdout = echo.main(args)
        usage = "Hello"
        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
