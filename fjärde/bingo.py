def get_vert_set(bingo, index):
    vert_set = set()
    for row in bingo:
        vert_set.add(row[index])
    return vert_set


def get_hori_set(bingo, index):
    hori_set = set()
    for i, ele in enumerate(bingo[index]):
        hori_set.add(bingo[index][i])
    return hori_set


def get_total_set(bingo):
    tot = set()
    for row in bingo:
        for num in row:
            tot.add(num)
    return tot


def get_winner(instructions, bingolist):
    ins_set = set()
    winlist = []
    for ins_num, instruction in enumerate(instructions):
        ins_set.add(instruction)
        for i,  bingo in enumerate(bingolist):
            if i not in winlist:
                for index, coord in enumerate(bingo):
                    vert = get_vert_set(bingo, index)
                    hori = get_hori_set(bingo, index)
                    if vert.issubset(ins_set) or hori.issubset(ins_set):

                        winlist.append(i)
                        lastwinner = bingo
                        last_inst = instruction
                        ins_history  =set(list(ins_set))
                        break

    print(lastwinner, last_inst)

    rest_sum = sum(get_total_set(lastwinner)-(ins_history))
    return rest_sum*last_inst


bingolist = []

with open("fil.txt") as file:
    instructions = [int(x) for x in file.readline().split(",")]
    for line in file:
        if line == "\n":
            bingoline = []
            for i in range(5):
                row = [int(x) for x in file.readline().strip().split()]
                bingoline.append(row)
            bingolist.append(bingoline)

print(get_winner(instructions, bingolist))
