split_text = ((open("day4.txt")).read()).split("\n")
counter1 = 0 
counter2 = 0 
for i in range(len(split_text)):

    
    line = split_text[i].split(",")
   
    group1 = line[0].split("-")
    group2 = line[1].split("-")
   
    fullgroup = group1 + group2
   
    for x in range(len(fullgroup)):
        fullgroup[x] = int(fullgroup[x])
    print(fullgroup)


    if fullgroup[3] >= fullgroup[1] and fullgroup[2] <= fullgroup[0]:
        counter1 += 1
    elif fullgroup[1] >= fullgroup[3] and fullgroup[2] >= fullgroup[0]:
        counter1 += 1

    fullrange1 = list(range(fullgroup[0], fullgroup[1] + 1))
    fullrange2 = list(range(fullgroup[2], fullgroup[3] + 1))

    if any(x in fullrange1 for x in fullrange2):
        counter2 += 1
    elif any(x in fullrange2 for x in fullrange1):
        counter2 += 1

print(counter1)
print(counter2)




