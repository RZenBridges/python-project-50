import json


def generate_diff(file_path1, file_path2):
    difference = "{\n"
    file_json1 = json.load(open(file_path1))
    file_json2 = json.load(open(file_path2))
    key_set1 = list(file_json1.keys())
    key_set2 = list(file_json2.keys())
    for key1 in key_set1:
        if key1 in key_set2 and file_json1[key1] == file_json2[key1]:
            difference += f"    {key1}: {file_json1[key1]}\n"
        elif key1 not in key_set2:
            difference += f"  - {key1}: {file_json1[key1]}\n"
        elif key1 in key_set2 and file_json1[key1] != file_json2[key1]:
            difference += f"  - {key1}: {file_json1[key1]}\n  + {key1}: {file_json2[key1]}\n"
    for key2 in key_set2:
        if key2 not in key_set1:
            difference += f"  + {key2}: {file_json2[key2]}\n"
    difference += "}"
    print(difference)
    return difference

#generate_diff('/home/istari/file1.json', '/home/istari/file2.json')
