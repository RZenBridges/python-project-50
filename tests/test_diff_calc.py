from gendiff.diff_calc import build_diff, parse_file


def test_build_diff_recursive_1():
    with open('tests/fixtures/recursive_result.txt', 'r') as data:
        control = data.read().strip().split('\n\n')
        file1 = parse_file('tests/fixtures/file1.json')
        file2 = parse_file('tests/fixtures/file2.json')
        out = build_diff(file1, file2)
        assert str(out) == control[0]


def test_build_diff_recursive_2():
    with open('tests/fixtures/recursive_result.txt', 'r') as data:
        control = data.read().strip().split('\n\n')
        file1 = parse_file('tests/fixtures/file1.yml')
        file2 = parse_file('tests/fixtures/file2.yml')
        out = build_diff(file1, file2)
        assert str(out) == control[0]


def test_build_diff_recursive_3():
    with open('tests/fixtures/recursive_result.txt', 'r') as data:
        control = data.read().strip().split('\n\n')
        file1 = parse_file('tests/fixtures/file5.yml')
        file2 = parse_file('tests/fixtures/file6.yml')
        out = build_diff(file1, file2)
        assert str(out) == control[1]
