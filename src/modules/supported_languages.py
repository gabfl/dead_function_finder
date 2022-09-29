languages = {
    'python': {
        'search_pattern_start': r'(\.|\s)',
        'search_pattern_end': '(\s)?\(',
        'function_definition_pattern': r'def\s(\w+)\(',
        'magic_method_format': r'^__.*__$',
        'extension': '.py'
    },
    'php': {
        'search_pattern_start': r'(>|::)',
        'search_pattern_end': '(\s)?\(',
        'function_definition_pattern': r'function\s+([^\s\(]+)\s*\(',
        'magic_method_format': r'^__.*$',
        'extension': '.php'
    },
}


def get_extension(language):
    """ Return the extension of a language """

    try:
        return languages[language]['extension']
    except KeyError:
        raise NotImplementedError


def get_function_definition_pattern(language):
    """ Return functions definition pattern """

    try:
        return languages[language]['function_definition_pattern']
    except KeyError:
        raise NotImplementedError


def get_magic_method_format(language):
    """ Return magic method format """

    try:
        return languages[language]['magic_method_format']
    except KeyError:
        raise NotImplementedError


def get_search_pattern(language):
    """ Return search pattern """

    try:
        return (languages[language]['search_pattern_start'], languages[language]['search_pattern_end'])
    except KeyError:
        raise NotImplementedError
