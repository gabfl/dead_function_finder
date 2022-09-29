
import argparse

from .modules.function_finder import find_all_functions_in_path


def main():
    """ Return a list of functions within a directory """

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--language", type=str, help="Programming language",
                        choices=['python', 'php'], default='python')
    parser.add_argument(
        "-p", "--path", help="Path to directory", required=True)
    args = parser.parse_args()

    # Define extension
    extension = '.py' if args.language == 'python' else '.php'

    functions_by_file = find_all_functions_in_path(args.path, extension)
    functions_count = sum(len(v) for v in functions_by_file.values())
    print(' * Found {} functions in {} files.'.format("{:,.0f}".format(functions_count),
                                                      "{:,.0f}".format(len(functions_by_file))))

    # print(all_functions)
    # print(len(all_functions))
    return None


if __name__ == '__main__':
    main()
