text = open("ethan5.txt").read()
text = text.split("\n")
stacks_initializer = text[0:8]
instructions = text[10::]

stacks = []

for i in range(0, 9):
    stacks.append([])

for line in stacks_initializer:
    for i in range(0,9):
        if line[i * 4 + 1] == " ":
            continue
        stacks[i].append(line[i * 4 + 1])

for instruction in instructions:
    print(instruction)
    instruction = instruction.split(" ")
    crate_number = int(instruction[1])
    initial_crate_index = int(instruction[3]) - 1
    final_crate_index = int(instruction[5]) - 1
    to_be_added = []
    for i in range(0, crate_number):
        # stacks[final_crate_index].insert(0, stacks[initial_crate_index].pop(0))
        to_be_added.append(stacks[initial_crate_index].pop(0))
    for crate in reversed(to_be_added):
        stacks[final_crate_index].insert(0, crate)


for stack in stacks:
    print(stack)
first_crates = ""
for stack in stacks:
    first_crates += stack[0]
print(first_crates)