split_text = ((open("day3.txt")).read()).split("\n")

valueCount = 0 
valueCount2 = 0

BAD = {
1: "a",
2: "b",
3: "c",
4: "d",
5: "e",
6: "f",
7: "g",
8: "h",
9: "i",
10: "j",
11: "k",
12: "l",
13: "m",
14: "n",
15: "o",
16: "p",
17: "q",
18: "r",
19: "s",
20: "t",
21: "u",
22: "v",
23: "w",
24: "x",
25: "y",
26: "z",
27: "A",
28: "B",
29: "C",
30: "D",
31: "E",
32: "F",
33: "G",
34: "H",
35: "I",
36: "J",
37: "K",
38: "L",
39: "M",
40: "N",
41: "O",
42: "P",
43: "Q",
44: "R",
45: "S",
46: "T",
47: "U",
48: "V",
49: "W",
50: "X",
51: "Y",
52: "Z"
}

#change all the strings above to arrays of strings

for i in range(len(split_text)):
    halfPos = len(split_text[i]) / 2
    listedText = list(split_text[i])
    halfPoint = len(listedText)/2
    print(halfPoint)
    halfPoint = int(halfPoint)
    firstSack = listedText[:halfPoint]
    print(firstSack)
    secondSack = listedText[halfPoint:]
    print(secondSack)
    commonValue = [c for c in firstSack if c in secondSack]
    cm1 = commonValue[0]
    print(cm1)
    for key, values in BAD.items():
        if values == cm1:
            valueCount += key
print(valueCount)

pos1 = 0
pos2 = 1
pos3 = 2


for i in range(100):
    elf1 = list(split_text[(i*3) + pos1])
    elf2 = list(split_text[(i*3) + pos2])
    elf3 = list(split_text[(i*3) + pos3])
    common1 = [c for c in elf1 if c in elf2]
    common2 = [c for c in common1 if c in elf3]
    print(common2)
    finalval = common2[0]
    for key, values in BAD.items():
        if values == finalval:
            valueCount2 += key
print(valueCount)





