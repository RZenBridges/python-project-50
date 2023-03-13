from gendiff.read_file import yaml_to_text, json_to_text
from pathlib import PurePosixPath, PureWindowsPath
import platform


def parse_file(path):
    if platform.system() == 'Linux':
        file_name = PurePosixPath(path).name
    elif platform.system() == 'Windows':
        file_name = PureWindowsPath(path).name
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        return yaml_to_text(path)
    if file_name.endswith('.json'):
        return json_to_text(path)
