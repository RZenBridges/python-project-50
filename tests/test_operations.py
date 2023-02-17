from gendiff.operations import generate_diff


def test_generate_diff_1():
    with open('tests/fixtures/test_result1.txt', 'r') as data:
         assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == data.read()


def test_generate_diff_2():
    with open('tests/fixtures/test_result2.txt', 'r') as data:
        assert generate_diff('tests/fixtures/file2.json', 'tests/fixtures/file1.json') == data.read()

def test_generate_diff_3():
    with open('tests/fixtures/test_result3.txt', 'r') as data:
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file3.json') == data.read()
