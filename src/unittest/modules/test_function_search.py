import unittest
import os

from ...modules import function_search


class Test(unittest.TestCase):

    def test_search_function_in_file(self):
        # Location of test file
        os.chdir(os.path.dirname(__file__))
        file_path = os.getcwd() + '/../assets/test_codebase/python/one.py'

        # assert function_search.search_function_in_file(
        #     'some_function', file_path, 'python') is True
        assert function_search.search_function_in_file(
            'i_am_invalid', file_path, 'python') is False

        file_path = os.getcwd() + '/../assets/test_codebase/php/one.php'
        # assert function_search.search_function_in_file(
        #     'some_function', file_path, 'php') is True
        assert function_search.search_function_in_file(
            'i_am_invalid', file_path, 'php') is False

    def test_iterate_and_search(self):
        # Location of test file
        os.chdir(os.path.dirname(__file__))
        files = [
            os.getcwd() + '/../assets/test_codebase/python/one.py',
            os.getcwd() + '/../assets/test_codebase/python/two.py'
        ]

        # assert function_search.iterate_and_search(
        #     'some_function', files, 'python') is True
        assert function_search.iterate_and_search(
            'i_am_invalid', files, 'python') is False
