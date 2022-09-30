import unittest
import os

from ...modules import supported_languages


class Test(unittest.TestCase):

    def test_supported_languages(self):

        assert isinstance(supported_languages.languages, dict)

        for language in supported_languages.languages:
            values = supported_languages.languages[language]
            assert isinstance(language, str)
            assert isinstance(values, dict)
            assert isinstance(values['search_pattern_start'], str)
            assert isinstance(values['search_pattern_end'], str)
            assert isinstance(values['function_definition_pattern'], str)
            assert isinstance(values['magic_method_format'], str)
            assert isinstance(values['extension'], str)

    def test_get_extension(self):
        assert supported_languages.get_extension('python') == '.py'
        assert supported_languages.get_extension('php') == '.php'
        with self.assertRaises(NotImplementedError):
            supported_languages.get_extension('exe')

    def test_get_function_definition_pattern(self):
        assert supported_languages.get_function_definition_pattern(
            'python') == r'def\s(\w+)\('
        with self.assertRaises(NotImplementedError):
            supported_languages.get_function_definition_pattern('exe')

    def test_get_magic_method_format(self):
        assert supported_languages.get_magic_method_format(
            'python') == r'^__.*__$'
        with self.assertRaises(NotImplementedError):
            supported_languages.get_magic_method_format('exe')

    def test_get_search_pattern(self):
        assert isinstance(
            supported_languages.get_search_pattern('python'), tuple)
        with self.assertRaises(NotImplementedError):
            supported_languages.get_search_pattern('exe')
