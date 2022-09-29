import unittest
import os

from ...modules import function_finder, directory_parser


class Test(unittest.TestCase):

    def test_find_functions_py(self):
        # Location of test file
        os.chdir(os.path.dirname(__file__))
        file_path = os.getcwd() + '/../assets/test_codebase/python/one.py'

        # Get functions
        functions = function_finder.find_functions(file_path, 'python')
        functions.sort()

        assert isinstance(functions, list)
        assert functions == ['dead_function',
                             'some_function', 'some_other_function']

    def test_find_functions_php(self):
        # Location of test file
        os.chdir(os.path.dirname(__file__))
        file_path = os.getcwd() + '/../assets/test_codebase/php/one.php'

        # Get functions
        functions = function_finder.find_functions(file_path, 'php')
        functions.sort()

        assert isinstance(functions, list)
        assert functions == ['dead_function',
                             'some_function', 'some_other_function']

    def test_find_functions_invalid_ext(self):
        # Location of test file
        os.chdir(os.path.dirname(__file__))
        file_path = os.getcwd() + '/../assets/test_codebase/php/one.php'

        # Get functions
        with self.assertRaises(NotImplementedError):
            function_finder.find_functions(file_path, 'exe')

    def test_find_all_functions(self):
        # Location of test file
        os.chdir(os.path.dirname(__file__))
        path = os.getcwd() + '/../assets/test_codebase/python/'

        # Get functions
        all_files = [x for x in directory_parser.parse(path, 'python')]
        functions_by_file = function_finder.find_all_functions(
            all_files, 'python')

        assert isinstance(functions_by_file, dict)
        for filename in functions_by_file:
            assert isinstance(filename, str)
            assert isinstance(functions_by_file[filename], list)

    def test_remove_magic_methods(self):
        functions = ['__init__', '__init__', 'hello', 'world', '__str__']
        functions = function_finder.remove_magic_methods(functions, 'python')
        assert functions == ['hello', 'world']

        functions = ['__construct', '__destruct', 'hello', 'world']
        functions = function_finder.remove_magic_methods(functions, 'php')
        assert functions == ['hello', 'world']
