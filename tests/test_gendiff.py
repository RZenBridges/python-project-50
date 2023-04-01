import pytest
from gendiff import generate_diff
from gendiff.files import read_file


INPUT_JSON_FILE_1 = 'tests/fixtures/input_files/file1.json'
INPUT_JSON_FILE_2 = 'tests/fixtures/input_files/file2.json'
INPUT_YML_FILE_5 = 'tests/fixtures/input_files/file5.yml'
INPUT_YML_FILE_6 = 'tests/fixtures/input_files/file6.yml'
INPUT_JSON_FILE_7 = 'tests/fixtures/input_files/file7.json'
INPUT_JSON_FILE_8 = 'tests/fixtures/input_files/file8.json'



@pytest.mark.parametrize(
    'file1,file2,expected_result_file', [
        (INPUT_YML_FILE_5, INPUT_YML_FILE_6,
         'tests/fixtures/format_stylish_56.txt'),
        (INPUT_JSON_FILE_7, INPUT_JSON_FILE_8,
         'tests/fixtures/format_stylish_78.txt'),
    ])
def test_gendiff_stylish(file1, file2, expected_result_file):
    diff = generate_diff(file1, file2, format='stylish')
    assert diff == read_file(expected_result_file)


@pytest.mark.parametrize(
    'file1,file2,expected_result_file', [
        (INPUT_YML_FILE_5, INPUT_YML_FILE_6,
         'tests/fixtures/format_plain_56.txt'),
        (INPUT_JSON_FILE_7, INPUT_JSON_FILE_8,
         'tests/fixtures/format_plain_78.txt'),
    ])
def test_gendiff_plain(file1, file2, expected_result_file):
    diff = generate_diff(file1, file2, format='plain')
    assert diff == read_file(expected_result_file)


@pytest.mark.parametrize(
    'file1,file2,expected_result_file', [
        (INPUT_JSON_FILE_1, INPUT_JSON_FILE_2,
         'tests/fixtures/format_json.txt')
    ])
def test_gendiff_json(file1, file2, expected_result_file):
    diff = generate_diff(file1, file2, format='json')
    assert diff == read_file(expected_result_file)
