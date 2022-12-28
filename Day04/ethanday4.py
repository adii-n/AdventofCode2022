text = open("ethan4.txt").read()
pairs = text.split("\n")

# pairs = pairs[0:1]

encompassed_count = 0
overlap_count = 0

for pair in pairs:
    # print(pair)
    assignments = pair.split(",")
    assignment1 = assignments[0]
    assignment2 = assignments[1]
    initial1 = int(assignment1.split("-")[0])
    final1 = int(assignment1.split("-")[1])
    initial2 = int(assignment2.split("-")[0])
    final2 = int(assignment2.split("-")[1])
    if (initial1 in range(initial2, final2+1)) and (final1 in range(initial2, final2+1)) or (initial2 in range(initial1, final1+1)) and (final2 in range(initial1, final1+1)):
        encompassed_count += 1
    if (initial1 in range(initial2, final2+1)) or (final1 in range(initial2, final2+1)) or (initial2 in range(initial1, final1+1)) or (final2 in range(initial1, final1+1)):
        overlap_count += 1
print(encompassed_count)
print(overlap_count)