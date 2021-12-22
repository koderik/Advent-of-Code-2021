cubelist = []
for x in range(-50, 51):
    ylist = []
    for y in range(-50, 51):
        zlist = []
        for z in range(-50, 51):
            zlist.append(False)
        ylist.append(zlist)
    cubelist.append(ylist)

with open("fil.txt") as file:
    for line in file:

        switcher = "on" in line
        data = line[line.index(" ") :].split(",")

        cl = []
        error = False
        for i in range(3):
            var1 = int(data[i][data[i].index("=") + 1 : data[i].index(".")])
            var2 = int(data[i][data[i].rindex(".") + 1 :])
            error = var1 > 50 or var2 < -50
            if error:
                break
            cl.append(var1)
            cl.append(var2)
        if not error:
            for i, var in enumerate(cl):
                if var < -50:
                    cl[i] = -50
                elif var > 50:
                    cl[i] = 50

            for x in range(cl[0], cl[1] + 1):
                for y in range(cl[2], cl[3] + 1):
                    for z in range(cl[4], cl[5] + 1):
                        cubelist[x][y][z] = switcher
cnt = 0
for x in cubelist:
    for y in x:
        for z in y:
            if z:
                cnt += 1
print(cnt)
