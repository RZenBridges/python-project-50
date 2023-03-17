from gendiff.format import stylish
from gendiff.format import plain
from gendiff.format import jsonify


CHOICES = ['stylish', 'plain', 'json']


def formatter(arg: str):
    action = {'stylish': stylish.render,
              'plain': plain.render,
              'json': jsonify.render}
    return action[arg]
