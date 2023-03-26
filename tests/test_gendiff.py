import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    'file1,file2,expected', [
        ('tests/fixtures/input_files/file1.json',
         'tests/fixtures/input_files/file2.json',
         'tests/fixtures/format_stylish_12.txt'),
        ('tests/fixtures/input_files/file5.yml',
         'tests/fixtures/input_files/file6.yml',
         'tests/fixtures/format_stylish_56.txt')
    ])
def test_gendiff_main(file1, file2, expected):
    with open(expected) as control:
        result = control.read().strip()
    out = generate_diff(file1, file2)
    assert out == result
