

tal = []
rows = 1
with open("fil.txt") as file:
    first = file.readline().strip()
    for char in first:
        tal.append(int(char))
    for line in file:
        rows += 1
        for i, char in enumerate(line.strip()):
            tal[i] += int(char)

tal = [round(x/rows) for x in tal]
combined = [str(x) for x in tal]
inverse = ["0" if x in "1" else "1" for x in combined]
combined = ("").join(combined)
inverse = ("").join(inverse)
tal = int(combined,2)
tal_inv = int(inverse, 2)
print(tal)
print(tal_inv)
print(tal*tal_inv)