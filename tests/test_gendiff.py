import pytest

from gendiff import generate_diff
from gendiff.files import read_file
from gendiff.format import STYLISH, PLAIN, JSON


INPUT_YML_FILE_1 = 'tests/fixtures/input_files/file1.yml'
INPUT_YML_FILE_2 = 'tests/fixtures/input_files/file2.yml'
INPUT_JSON_FILE_1 = 'tests/fixtures/input_files/file1.json'
INPUT_JSON_FILE_2 = 'tests/fixtures/input_files/file2.json'


@pytest.mark.parametrize(
    'file1,file2,expected_result_file', [
        (INPUT_YML_FILE_1, INPUT_YML_FILE_2,
         'tests/fixtures/format_stylish_12_yml.txt'),
        (INPUT_JSON_FILE_1, INPUT_JSON_FILE_2,
         'tests/fixtures/format_stylish_12_json.txt'),
    ])
def test_gendiff_stylish(file1, file2, expected_result_file):
    diff = generate_diff(file1, file2, format=STYLISH)
    assert diff == read_file(expected_result_file)


@pytest.mark.parametrize(
    'file1,file2,expected_result_file', [
        (INPUT_YML_FILE_1, INPUT_YML_FILE_2,
         'tests/fixtures/format_plain_12_yml.txt'),
        (INPUT_JSON_FILE_1, INPUT_JSON_FILE_2,
         'tests/fixtures/format_plain_12_json.txt'),
    ])
def test_gendiff_plain(file1, file2, expected_result_file):
    diff = generate_diff(file1, file2, format=PLAIN)
    assert diff == read_file(expected_result_file)


@pytest.mark.parametrize(
    'file1,file2,expected_result_file', [
        (INPUT_JSON_FILE_1, INPUT_JSON_FILE_2,
         'tests/fixtures/format_json.txt')
    ])
def test_gendiff_json(file1, file2, expected_result_file):
    diff = generate_diff(file1, file2, format=JSON)
    assert diff == read_file(expected_result_file)
