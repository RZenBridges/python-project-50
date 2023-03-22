import pytest
from gendiff.data_parsing import read_and_parse_file


with open('tests/fixtures/file1.txt', 'r') as data:
    expected_result_1 = data.read().strip()


with open('tests/fixtures/file2.txt', 'r') as data:
    expected_result_2 = data.read().strip()


input_1 = str(read_and_parse_file('tests/fixtures/file1.json'))
input_2 = str(read_and_parse_file('tests/fixtures/file2.json'))
input_3 = str(read_and_parse_file('tests/fixtures/file1.yml'))
input_4 = str(read_and_parse_file('tests/fixtures/file2.yml'))


@pytest.mark.parametrize(
    'test_input,expected', [
        (input_1, expected_result_1),
        (input_2, expected_result_2),
        (input_3, expected_result_1),
        (input_4, expected_result_2)
    ])
def test_read_and_parse_file(test_input, expected):
    assert test_input == expected
