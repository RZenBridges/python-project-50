import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    'file1,file2,expected,format', [
        ('tests/fixtures/input_files/file1.json',
         'tests/fixtures/input_files/file2.json',
         'tests/fixtures/format_stylish_12.txt',
         'stylish'),
        ('tests/fixtures/input_files/file5.yml',
         'tests/fixtures/input_files/file6.yml',
         'tests/fixtures/format_stylish_56.txt',
         'stylish'),
        ('tests/fixtures/input_files/file7.json',
         'tests/fixtures/input_files/file8.json',
         'tests/fixtures/format_stylish_78.txt',
         'stylish'),
        ('tests/fixtures/input_files/file1.json',
         'tests/fixtures/input_files/file2.json',
         'tests/fixtures/format_plain_12.txt',
         'plain'),
        ('tests/fixtures/input_files/file5.yml',
         'tests/fixtures/input_files/file6.yml',
         'tests/fixtures/format_plain_56.txt',
         'plain'),
        ('tests/fixtures/input_files/file7.json',
         'tests/fixtures/input_files/file8.json',
         'tests/fixtures/format_plain_78.txt',
         'plain'),
        ('tests/fixtures/input_files/file1.json',
         'tests/fixtures/input_files/file2.json',
         'tests/fixtures/format_json.txt',
         'json')
    ])
def test_gendiff_main(file1, file2, expected, format):
    with open(expected) as control:
        result = control.read().strip()
    out = generate_diff(file1, file2, format)
    assert out == result
