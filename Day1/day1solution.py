inputFile = (open("day1.txt")).read()
splitPerElf = inputFile.split("\n\n")
sumPerElf = []
for i in range(len(splitPerElf)):
    foodPerElf = sumPerElf[i].split("\n")
    sumPerElf.append(sum([int(x) for x in foodPerElf]))
sumPerElf.sort(reverse=True)
print("Part 1:", sumPerElf[0], " \nPart 2:", sum(sumPerElf[0:2]))
