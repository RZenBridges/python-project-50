from gendiff.data_parsing import adjust_format


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
    content1 = adjust_format(file_path1)
    content2 = adjust_format(file_path2)
    result = diff_check(content1, content2)
    print(result)
    return result

# generate_diff('/home/istari/file1.json', '/home/istari/file2.json')
