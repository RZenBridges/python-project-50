import argparse
import pathlib

import gendiff
from gendiff.format import FORMAT_CHOICES


def get_arguments():
    """ In CLI when utility 'gendiff' is called,
    the function returns a tuple (file1, file2, formatter) """
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        usage='%(prog)s [options] <filepath1> <filepath2>')
    parser.add_argument('first_file',
                        type=pathlib.Path,
                        help=argparse.SUPPRESS)
    parser.add_argument('second_file',
                        type=pathlib.Path,
                        help=argparse.SUPPRESS)
    parser.add_argument('-V',
                        '--version',
                        dest='version',
                        help='output the version number',
                        action='version',
                        version=f'%(prog)s {gendiff.__version__}')
    parser.add_argument('-f',
                        '--format',
                        help='output format (default: "%(default)s")',
                        choices=FORMAT_CHOICES.keys(),
                        metavar='',
                        default='stylish')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
