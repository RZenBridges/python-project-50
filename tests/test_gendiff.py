import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    'file1,file2,format,expected_result', [
        ('tests/fixtures/input_files/file1.json',
         'tests/fixtures/input_files/file2.json',
         'stylish',
         'tests/fixtures/format_stylish_12.txt'),
        ('tests/fixtures/input_files/file5.yml',
         'tests/fixtures/input_files/file6.yml',
         'stylish',
         'tests/fixtures/format_stylish_56.txt'),
        ('tests/fixtures/input_files/file7.json',
         'tests/fixtures/input_files/file8.json',
         'stylish',
         'tests/fixtures/format_stylish_78.txt'),
    ])
def test_gendiff_stylish(file1, file2, format, expected_result):
    with open(expected_result) as data:
        expected_diff = data.read().strip()
    diff = generate_diff(file1, file2, format)
    assert diff == expected_diff


@pytest.mark.parametrize(
    'file1,file2,format,expected_result', [
        ('tests/fixtures/input_files/file1.json',
         'tests/fixtures/input_files/file2.json',
         'plain',
         'tests/fixtures/format_plain_12.txt'),
        ('tests/fixtures/input_files/file5.yml',
         'tests/fixtures/input_files/file6.yml',
         'plain',
         'tests/fixtures/format_plain_56.txt'),
        ('tests/fixtures/input_files/file7.json',
         'tests/fixtures/input_files/file8.json',
         'plain',
         'tests/fixtures/format_plain_78.txt'),
    ])
def test_gendiff_plain(file1, file2, format, expected_result):
    with open(expected_result) as data:
        expected_diff = data.read().strip()
    diff = generate_diff(file1, file2, format)
    assert diff == expected_diff


@pytest.mark.parametrize(
    'file1,file2,format,expected_result', [
        ('tests/fixtures/input_files/file1.json',
         'tests/fixtures/input_files/file2.json',
         'json',
         'tests/fixtures/format_json.txt')
    ])
def test_gendiff_json(file1, file2, format, expected_result):
    with open(expected_result) as data:
        expected_diff = data.read().strip()
    diff = generate_diff(file1, file2, format)
    assert diff == expected_diff
