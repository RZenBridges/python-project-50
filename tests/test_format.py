from gendiff.format import stylish, plain, jsonify


with open('tests/fixtures/recursive_result.txt') as input:
    data = input.read().split('\n\n')
    input_check_1 = data[0]
    input_check_2 = data[1]


def test_stylish_1():
    with open('tests/fixtures/format_stylish.txt') as data:
        result = data.read().strip().split('\n\n\n')
        assert stylish.render(eval(input_check_1)) == result[0]


def test_stylish_2():
    with open('tests/fixtures/format_stylish.txt') as data:
        result = data.read().strip().split('\n\n\n')
        assert stylish.render(eval(input_check_2)) == result[1]


def test_plain_1():
    with open('tests/fixtures/format_plain.txt') as data:
        result = data.read().strip().split('\n\n\n')
        assert plain.render(eval(input_check_1)) == result[0]


def test_plain_2():
    with open('tests/fixtures/format_plain.txt') as data:
        result = data.read().strip().split('\n\n\n')
        assert plain.render(eval(input_check_2)) == result[1]


def test_jsonify_1():
    with open('tests/fixtures/format_json.txt') as data:
        assert jsonify.render(eval(input_check_1)) == data.read().strip()
