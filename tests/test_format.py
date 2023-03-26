import pytest
from gendiff.format import stylish, plain, jsonify


@pytest.mark.parametrize(
    'test_input,expected', [
        ('tests/fixtures/recursive_result_12.txt',
         'tests/fixtures/format_stylish_12.txt'),
        ('tests/fixtures/recursive_result_56.txt',
         'tests/fixtures/format_stylish_56.txt')
    ])
def test_stylish(test_input, expected):
    with open(expected) as data:
        result = data.read().strip()
    with open(test_input) as data:
        file = eval(data.read())
    out = stylish.render(file)
    assert out == result


@pytest.mark.parametrize(
    'test_input,expected', [
        ('tests/fixtures/recursive_result_12.txt',
         'tests/fixtures/format_plain_12.txt'),
        ('tests/fixtures/recursive_result_56.txt',
         'tests/fixtures/format_plain_56.txt')
    ])
def test_plain(test_input, expected):
    with open(expected) as data:
        result = data.read().strip()
    with open(test_input) as data:
        file = eval(data.read())
    out = plain.render(file)
    assert out == result


@pytest.mark.parametrize(
    'test_input,expected', [
        ('tests/fixtures/recursive_result_12.txt',
         'tests/fixtures/format_json.txt')
    ])
def test_jsonify(test_input, expected):
    with open(expected) as data:
        result = data.read().strip()
    with open(test_input) as data:
        file = eval(data.read())
    out = jsonify.render(file)
    assert out == result
