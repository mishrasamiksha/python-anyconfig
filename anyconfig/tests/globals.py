#
# Copyright (C) 2013 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
import anyconfig.globals as TT
import unittest


class Test_00(unittest.TestCase):

    def test_logger_instance(self):
        self.assertTrue(isinstance(TT.LOGGER, TT.logging.Logger))

# vim:sw=4:ts=4:et:
