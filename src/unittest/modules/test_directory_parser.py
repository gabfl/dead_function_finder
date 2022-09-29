import unittest
import types
import os

from ...modules import directory_parser


class Test(unittest.TestCase):

    def test_parse(self):
        os.chdir(os.path.dirname(__file__))

        parsed = directory_parser.parse(
            os.getcwd() + '/../assets/test_codebase/python', '.py')
        assert isinstance(parsed, types.GeneratorType)

        i = 0
        for full_path in parsed:
            filename = full_path.split('/')[-1]
            assert filename in ['one.py', 'two.py', 'three.py']
            i += 1
        assert i == 3

    def test_parse_not_found(self):
        # with self.assertRaises(FileNotFoundError):
        #     directory_parser.parse('/tmp/dir/not_found', '.php')
        pass

    def test_resolve_home_path(self):
        path = directory_parser.resolve_home_path('~/')
        assert path == os.path.expanduser('~/')
