import unittest
import os
import sys

from .. import dead_function_finder


class Test(unittest.TestCase):

    def test_main(self):
        # Location of test file
        os.chdir(os.path.dirname(__file__))
        path = os.getcwd() + '/assets/test_codebase/python'

        # Define argparse inputs
        sys.argv = ['dead_function_finder', '--path', path, '-l', 'python']

        res = dead_function_finder.main()
        assert res is None
