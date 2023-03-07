from gendiff.operations import diff_check, adjust_format


def test_generate_diff_recursive_1():
    with open('tests/fixtures/recursive_result.txt', 'r') as data:
        out = diff_check(adjust_format('tests/fixtures/file1.json'), adjust_format('tests/fixtures/file2.json'))
        assert str(out) == data.read().strip()


def test_generate_diff_recursive_2():
    with open('tests/fixtures/recursive_result.txt', 'r') as data:
        out = diff_check(adjust_format('tests/fixtures/file1.yml'), adjust_format('tests/fixtures/file2.yml'))
        assert str(out) == data.read().strip()
