from gendiff.data_parsing import adjust_format


def test_adjust_format1():
    with open('tests/fixtures/file1.txt', 'r') as data:
        result = str(adjust_format('tests/fixtures/file1.json'))
        assert result == data.read().strip()


def test_adjust_format2():
    with open('tests/fixtures/file2.txt', 'r') as data:
        result = str(adjust_format('tests/fixtures/file2.json'))
        assert result == data.read().strip()


def test_adjust_format3():
    with open('tests/fixtures/file1.txt', 'r') as data:
        result = str(adjust_format('tests/fixtures/file1.yml'))
        assert result == data.read().strip()


def test_adjust_format4():
    with open('tests/fixtures/file2.txt', 'r') as data:
        result = str(adjust_format('tests/fixtures/file2.yml'))
        assert result == data.read().strip()
