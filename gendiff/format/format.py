from gendiff.format import stylish
from gendiff.format import plain
from gendiff.format import jsonify


STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'

FORMAT_CHOICES = {
    STYLISH: stylish.render,
    PLAIN: plain.render,
    JSON: jsonify.render
}


def get_format_handler(format_option):
    return FORMAT_CHOICES[format_option]
