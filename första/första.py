counter = 0
array = []
with open("fil.txt") as file:
    talen = [int(a) for a in file.readlines()]
    for i in range(0, len(talen) - 2):
        sum = 0
        for j in range(3):
            sum += talen[i + j]
        array.append(sum)

prev = array[0]
for line in array:
    if line > prev:
        counter += 1
    prev = line

print(counter)
