from gendiff.format import stylish
from gendiff.format import plain
from gendiff.format import jsonify


CHOICES = ['stylish', 'plain', 'json']


def formatter(format_option):
    action = {'stylish': stylish.render,
              'plain': plain.render,
              'json': jsonify.render}
    return action[format_option]
