import argparse
import gendiff
from gendiff.format import CHOICES
import pathlib


def cli_call():
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
                        dest='form',
                        choices=CHOICES,
                        metavar='',
                        default='stylish')
    return parser.parse_args()
