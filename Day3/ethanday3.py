text = (open("ethan3.txt")).read()
text = text.split("\n")

matches = []

for rucksack in text:
    compartment1 = rucksack[:len(rucksack) // 2]
    compartment2 = rucksack[len(rucksack) // 2 : len(rucksack)]
    for i in range(0, len(compartment1)):
        for j in range(0, len(compartment2)):
            if compartment1[i] == compartment2[j]:
                match = compartment1[i]
                break
    matches += match
priorities = []
for match in matches:
    if match.isupper():
        toBeAdded = ord(match) - ord('A') + 27
    else:
        toBeAdded = ord(match) - ord('a') + 1
    priorities.append(toBeAdded)

groups = []
for i in range(0, len(text), 3):
    groups.append(text[i:i+3])
print(groups)
badges = []
for group in groups:
    elf1 = group[0]
    elf2 = group[1]
    elf3 = group[2]
    for i in range(0, len(elf1)):
        for j in range(0, len(elf2)):
            for k in range(0, len(elf3)):
                if elf1[i] == elf2[j] == elf3[k]:
                    badge = elf1[i]
                    break
    badges.append(badge)
badgeValues = []
for badge in badges:
    if badge.isupper():
        toBeAdded = ord(badge) - ord('A') + 27
    else:
        toBeAdded = ord(badge) - ord('a') + 1
    badgeValues.append(toBeAdded)
print(badgeValues)
print(sum(badgeValues))