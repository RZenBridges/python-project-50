from gendiff.scripts.gendiff import main
import os


def test_gendiff_main_1():
    os.system(f"poetry run gendiff -h > ./tests/fixtures/test_output.txt")
    with open('tests/fixtures/test_output_mark.txt') as control:
        with open('tests/fixtures/test_output.txt') as sample:
            assert control.read().strip() == sample.read().strip()


def test_gendiff_main_2():
    os.system(f"poetry run gendiff tests/fixtures/file3.json tests/fixtures/file4.yml > ./tests/fixtures/test_stylish_output")
    with open('tests/fixtures/format_stylish.txt') as control:
        with open('tests/fixtures/test_stylish_output') as sample:
            assert control.read().strip().split('\n\n\n')[1] == sample.read().strip()


def test_gendiff_main_3():
    os.system(f"poetry run gendiff -f plain tests/fixtures/file3.json tests/fixtures/file4.yml > ./tests/fixtures/test_plain_output")
    with open('tests/fixtures/format_plain.txt') as control:
        with open('tests/fixtures/test_plain_output') as sample:
            assert control.read().strip().split('\n\n\n')[1] == sample.read().strip()
