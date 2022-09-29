
import re

from .directory_parser import parse


def find_functions(file_path, extension='php'):
    """ Return a list of functions within a file """

    # Read file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Find all functions
    if extension == '.py':
        # Python
        functions = re.findall(r'def\s(\w+)\(', file_content)
    elif extension == '.php':
        functions = re.findall(r'function\s+([^\s\(]+)\s*\(', file_content)
    else:
        raise NotImplementedError

    # Remove magic methods
    functions = remove_magic_methods(functions, extension)

    return functions


def find_all_functions_in_path(path, extension='.py'):
    """ Return a list of functions within a directory """

    functions_by_file = {}
    for file_path in parse(path, extension):
        functions = find_functions(file_path, extension)
        functions_by_file[file_path] = functions

    return functions_by_file


def remove_magic_methods(functions, extension='.py'):
    """ Remove magic methods from a list of functions """

    # Remove magic methods
    result = []
    for function in functions:

        if extension == '.py':
            if function.startswith('__') and function.endswith('__'):
                continue
        elif extension == '.php':
            if function.startswith('__'):
                continue

        result.append(function)

    return result
