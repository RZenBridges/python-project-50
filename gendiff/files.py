def read_file(file_path):
    with open(file_path) as file:
        return file.read().strip()
