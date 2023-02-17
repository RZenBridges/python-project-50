import json


def path_to_json(file_path):
    return json.load(open(file_path))


def generate_diff(file_path1, file_path2):
    difference = "{\n"
    json1 = path_to_json(file_path1)
    json2 = path_to_json(file_path2)
    key_set1 = list(json1.keys())
    key_set2 = list(json2.keys())

    for k1 in key_set1:
        if k1 in key_set2 and json1[k1] == json2[k1]:
            difference += f"    {k1}: {json1[k1]}\n"
        elif k1 not in key_set2:
            difference += f"  - {k1}: {json1[k1]}\n"
        elif k1 in key_set2 and json1[k1] != json2[k1]:
            difference += f"  - {k1}: {json1[k1]}\n"
            difference += f"  + {k1}: {json2[k1]}\n"

    for k2 in key_set2:
        if k2 not in key_set1:
            difference += f"  + {k2}: {json2[k2]}\n"

    difference += "}\n"
    print(difference)
    return difference

# generate_diff('/home/istari/file1.json', '/home/istari/file2.json')
