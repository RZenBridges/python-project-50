import os


def test_gendiff_main_1():
    os.system("poetry run gendiff -h > ./tests/fixtures/test_output.txt")
    with open('tests/fixtures/test_output_mark.txt') as control:
        with open('tests/fixtures/test_output.txt') as sample:
            assert control.read().strip() == sample.read().strip()


def test_gendiff_main_2():
    file1 = 'tests/fixtures/file3.json'
    file2 = 'tests/fixtures/file4.yml'
    end_file = './tests/fixtures/test_stylish_output'
    os.system(f"poetry run gendiff {file1} {file2} > {end_file}")
    with open('tests/fixtures/format_stylish.txt') as control:
        with open('tests/fixtures/test_stylish_output') as sample:
            result = control.read().strip().split('\n\n\n')[1]
            assert result == sample.read().strip()


def test_gendiff_main_3():
    file1 = 'tests/fixtures/file3.json'
    file2 = 'tests/fixtures/file4.yml'
    end_file = './tests/fixtures/test_plain_output'
    os.system(f"poetry run gendiff -f plain {file1} {file2} > {end_file}")
    with open('tests/fixtures/format_plain.txt') as control:
        with open('tests/fixtures/test_plain_output') as sample:
            result = control.read().strip().split('\n\n\n')[1]
            assert result == sample.read().strip()
