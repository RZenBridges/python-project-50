from gendiff.format import jsonify
from gendiff.format import plain
from gendiff.format import stylish

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'

FORMAT_CHOICES = {
    STYLISH: stylish.render,
    PLAIN: plain.render,
    JSON: jsonify.render
}


def get_format_handler(format):
    try:
        result = FORMAT_CHOICES[format]
        return result
    except KeyError as missing:
        raise ValueError(f"Coundln't find the format "
                         f"{missing} inside format package")
