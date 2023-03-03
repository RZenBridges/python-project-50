from gendiff.gendiff_main import main
import os

def test_gendiff_main_1():
    os.system(f"poetry run gendiff -h > ./tests/fixtures/test_output.txt")
    with open('tests/fixtures/test_output_mark.txt') as control:
        with open('tests/fixtures/test_output.txt') as sample:
            assert control.read().strip() == sample.read().strip()
