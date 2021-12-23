def extract(list, index):
    sum = 0
    row_len = 0
    list = [row.strip() for row in list]
    for row in list:
        sum += int(row[index])
        row_len += 1
    if row_len == 1:
        return list
    ratio = sum/row_len
    if ratio == 1/2:
        common = 1
    else:
        common = round(ratio)

    new_list = []
    for row in list:
        if int(row[index]) == common:
            new_list.append(row)
    return new_list


def extract_i(list, index):
    sum = 0
    row_len = 0
    list = [row.strip() for row in list]
    for row in list:
        sum += int(row[index])
        row_len += 1
    if row_len == 1:
        return list
    ratio = sum/row_len
    if ratio == 1/2:
        common = 0
    else:
        num = round(ratio)
        if num == 0:
            common = 1
        else:
            common = 0
    new_list = []
    for row in list:
        if int(row[index]) == common:
            new_list.append(row)
    return new_list


with open("fil.txt") as file:
    binlist = file.readlines()
    copy = [x for x in binlist]
    width = len(binlist[0].strip())
    for i in range(width):
        binlist = extract(binlist, i)
        copy = extract_i(copy, i)
    print(binlist)
    print(copy)
    print(int(binlist[0], 2)*int(copy[0], 2))
