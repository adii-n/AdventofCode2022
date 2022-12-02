split_text = ((open("day2.txt")).read()).split("\n")

scoreSum = 0 

Dict = {
4 : ("A X"), 
8 : ("A Y"),
3 : ("A Z"),
1 : ("B X"),
5 : ("B Y"),
9 : ("B Z"),
7 : ("C X"),
2 : ("C Y"),
6 : ("C Z")
}

for i in range(len(split_text)):
    for key, value in Dict.items():
        if split_text[i] == value:
            scoreSum += key
print(scoreSum)

DictPt2 = {
3 : ("A X"),
4 : ("A Y"),
8 : ("A Z"),
1 : ("B X"),
5 : ("B Y"),
9 : ("B Z"),
2 : ("C X"),
6 : ("C Y"),
7 : ("C Z")
}
scoreSum2 = 0 
for i in range(len(split_text)):
    for key, value in DictPt2.items():
        if split_text[i] == value:
            scoreSum2 += key
print(scoreSum2)



