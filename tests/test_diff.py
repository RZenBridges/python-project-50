import pytest
from gendiff.diff import build_diff
from gendiff.data_parsing import read_and_parse_file


@pytest.mark.parametrize(
    'file1,file2,expected', [
        ('tests/fixtures/input_files/file1.json',
         'tests/fixtures/input_files/file2.json',
         'tests/fixtures/recursive_result_12.txt'),
        ('tests/fixtures/input_files/file5.yml',
         'tests/fixtures/input_files/file6.yml',
         'tests/fixtures/recursive_result_56.txt')
    ])
def test_build_diff(file1, file2, expected):
    with open(expected) as data:
        control = data.read().strip()
    out = build_diff(read_and_parse_file(file1),
                     read_and_parse_file(file2))
    assert str(out) == control
