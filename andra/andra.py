forward = 0
aim = 0
depth = 0

with open("fil.txt") as file:
    for line in file:
        if "forward" in line:
            tal = int(line[line.index(" ") :])
            forward += tal
            depth += aim * tal
        elif "down" in line:
            aim += int(line[line.index(" ") :])
        elif "up" in line:
            aim -= int(line[line.index(" ") :])
print(forward * depth)
