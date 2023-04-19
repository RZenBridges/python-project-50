import pytest
from gendiff import generate_diff
from gendiff.files import read_file
from gendiff.format import STYLISH, PLAIN, JSON


INPUT_JSON_FILE_1 = 'tests/fixtures/input_files/file1.json'
INPUT_JSON_FILE_2 = 'tests/fixtures/input_files/file2.json'
INPUT_YML_FILE_3 = 'tests/fixtures/input_files/file3.yml'
INPUT_YML_FILE_4 = 'tests/fixtures/input_files/file4.yml'
INPUT_JSON_FILE_5 = 'tests/fixtures/input_files/file5.json'
INPUT_JSON_FILE_6 = 'tests/fixtures/input_files/file6.json'


@pytest.mark.parametrize(
    'file1,file2,expected_result_file', [
        (INPUT_YML_FILE_3, INPUT_YML_FILE_4,
         'tests/fixtures/format_stylish_34.txt'),
        (INPUT_JSON_FILE_5, INPUT_JSON_FILE_6,
         'tests/fixtures/format_stylish_56.txt'),
    ])
def test_gendiff_stylish(file1, file2, expected_result_file):
    diff = generate_diff(file1, file2, format=STYLISH)
    assert diff == read_file(expected_result_file)


@pytest.mark.parametrize(
    'file1,file2,expected_result_file', [
        (INPUT_YML_FILE_3, INPUT_YML_FILE_4,
         'tests/fixtures/format_plain_34.txt'),
        (INPUT_JSON_FILE_5, INPUT_JSON_FILE_6,
         'tests/fixtures/format_plain_56.txt'),
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
