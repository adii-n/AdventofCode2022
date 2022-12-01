
text = open("day1.txt")
text = text.read()

split_text = text.split("\n\n")
all = [ ]
for i in range(len(split_text)):
    resplit_text = split_text[i].split("\n")
    for j in range(len(resplit_text)):
        resplit_text[j] = int(resplit_text[j]) 
    potentialGreatest = sum(resplit_text)
    all.append(potentialGreatest)

print(max(all))
all.sort()
all = all[::-1]
print(all)
top3 = all[0:3]
print(sum(top3))
