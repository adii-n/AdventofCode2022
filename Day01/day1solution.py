text = (open("day1.txt")).read()
split_text = text.split("\n\n")
all = []
for i in range(len(split_text)):
    resplit_text = split_text[i].split("\n")
    all.append(sum([int(x) for x in resplit_text]))
all.sort(reverse=True)
print("Part 1:", all[0], " \nPart 2:", sum(all[0:2]))
