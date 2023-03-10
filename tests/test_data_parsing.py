from gendiff.data_parsing import parse_file


def test_parse_file_1():
    with open('tests/fixtures/file1.txt', 'r') as data:
        result = str(parse_file('tests/fixtures/file1.json'))
        assert result == data.read().strip()


def test_parse_file_2():
    with open('tests/fixtures/file2.txt', 'r') as data:
        result = str(parse_file('tests/fixtures/file2.json'))
        assert result == data.read().strip()


def test_parse_file_3():
    with open('tests/fixtures/file1.txt', 'r') as data:
        result = str(parse_file('tests/fixtures/file1.yml'))
        assert result == data.read().strip()


def test_parse_file_4():
    with open('tests/fixtures/file2.txt', 'r') as data:
        result = str(parse_file('tests/fixtures/file2.yml'))
        assert result == data.read().strip()
