import time

start_time = time.time()


xyz = set()


def parse_row(line):
    switcher = "on" in line
    data = line[line.index(" "):].split(",")

    cl = []
    for i in range(3):
        var1 = int(data[i][data[i].index("=") + 1: data[i].index(".")])
        var2 = int(data[i][data[i].rindex(".") + 1:])
        cl.append(var1)
        cl.append(var2)

    for x in range(cl[0], cl[1] + 1):
        for y in range(cl[2], cl[3] + 1):
            for z in range(cl[4], cl[5] + 1):
                coord = (x, y, z)
                if switcher:
                    xyz.add(coord)
                else:
                    xyz.discard(coord)
    """
    xset = set(range(cl[0], cl[1] + 1))
    yset = set(range(cl[2], cl[3] + 1))
    zset = set(range(cl[4], cl[5] + 1))

    if switcher:
        x.update(xset)
        y.update(yset)
        z.update(zset)
    else:
        try:
            x.difference_update(xset)
            y.difference_update(yset)
            z.difference_update(zset)
        except KeyError:
            pass
    print(x,y,z)
    """


with open("fil.txt") as file:
    for line in file:
        parse_row(line)

#print(len(x) * len(y) * len(z))
print(len(xyz))
print("--- %s seconds ---" % (time.time() - start_time))
