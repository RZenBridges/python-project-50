from gendiff.format.f_stylish import stylish
from gendiff.format.f_plain import plain
from gendiff.format.f_json import jsonify


def format_of_choice(arg):
    if callable(arg):
        return arg
    action = {'stylish': stylish, 'plain': plain, 'json': jsonify}
    if isinstance(arg, str):
        return action[arg]


CHOICES = ['stylish', 'plain', 'json']
