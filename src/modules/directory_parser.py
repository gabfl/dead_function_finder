import glob
import re
import os


def parse(path, extension='.py'):
    """ Return a recursive list of files within a directory """

    # Add optional /
    if not path.endswith('/'):
        path += '/'

    # Resolve home path
    path = resolve_home_path(path)

    # Check if dir exists
    if not os.path.isdir(path):
        raise FileNotFoundError

    # absolute path to search all text files inside a specific folder
    path = path + r'**/*' + extension
    files = glob.glob(path, recursive=True)

    for file in files:
        yield file


def resolve_home_path(path):
    """ Resolve home path """

    if path.startswith('~'):
        path = os.path.expanduser(path)

    return path
