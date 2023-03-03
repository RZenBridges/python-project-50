from gendiff.format import stylish, plain, jsonify
import json


with open('tests/fixtures/recursive_result.txt') as input:
    line = ''
    for i in input.read().strip():
        if i != "'":
            line += i
        else:
            line += '"'
    input_check = json.loads(line)


def test_stylish_1():
    with open('tests/fixtures/format_stylish.txt') as data:
        assert stylish(input_check) == data.read().strip()


def test_plain_1():
    with open('tests/fixtures/format_plain.txt') as data:
        assert plain(input_check) == data.read().strip()

def test_jsonify():
    with open('tests/fixtures/format_json.txt') as data:
        assert jsonify(input_check) == data.read().strip()
