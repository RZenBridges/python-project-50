import json


def path_to_json(file_path):
    return json.load(open(file_path))


def diff_check(json1, json2):
    difference = "{\n"

    for k1 in json1:
        if k1 in json2 and json1[k1] == json2[k1]:
            difference += f"    {k1}: {json1[k1]}\n"
        elif (k1 not in json2) or (k1 in json2 and json1[k1] != json2[k1]):
            difference += f"  - {k1}: {json1[k1]}\n"

    for k2 in json2:
        if (k2 not in json1) or (k2 in json1 and json2[k2] != json1[k2]):
            difference += f"  + {k2}: {json2[k2]}\n"

    difference += "}\n"
    return difference


def generate_diff(file_path1, file_path2):
    json1 = path_to_json(file_path1)
    json2 = path_to_json(file_path2)
    result = diff_check(json1, json2)
    print(result)
    return result

# generate_diff('/home/istari/file1.json', '/home/istari/file2.json')
