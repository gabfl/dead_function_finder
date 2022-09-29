
import re

from .directory_parser import parse


def find_functions(file_path, language='python'):
    """ Return a list of functions within a file """

    # Read file
    with open(file_path, 'r') as file:
        try:
            file_content = file.read()
        except UnicodeDecodeError:
            return []

    # Find all functions
    if language == 'python':
        # Python
        functions = re.findall(r'def\s(\w+)\(', file_content)
    elif language == 'php':
        functions = re.findall(r'function\s+([^\s\(]+)\s*\(', file_content)
    else:
        raise NotImplementedError

    # Remove magic methods
    functions = remove_magic_methods(functions, language)

    return functions


def find_all_functions(files, language='python'):
    """ Return a list of functions within a directory """

    functions_by_file = {}
    for file_path in files:
        functions = find_functions(file_path, language)

        if functions:
            functions_by_file[file_path] = functions

    return functions_by_file


def remove_magic_methods(functions, language='python'):
    """ Remove magic methods from a list of functions """

    # Remove magic methods
    result = []
    for function in functions:

        if language == 'python':
            if function.startswith('__') and function.endswith('__'):
                continue
        elif language == 'php':
            if function.startswith('__'):
                continue

        result.append(function)

    return result
