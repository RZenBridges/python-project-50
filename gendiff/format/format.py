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


def get_format_handler(format):
    result = FORMAT_CHOICES.get(format)
    if result is None:
        print(f"Coundln't find the format {format} inside format package")
    else:
        return result
