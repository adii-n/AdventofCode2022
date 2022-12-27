text = open("ethan10.txt").read()
text = text.splitlines()

cycle_dict = {}

cycle = 1
x = 1

for i in range(0, len(text)):
    line = text[i]
    if line == "noop":
        cycle_dict[cycle] = x
        cycle += 1
    else:
        line = line.split(" ")
        cycle_dict[cycle] = x
        cycle += 1
        cycle_dict[cycle] = x
        cycle += 1 
        x += int(line[1])
    print("After line " + str(i + 1) + " cycle is " + str(cycle) + " and x is " + str(x))

# print(cycle_dict)

print(cycle_dict[20] * 20)
print(cycle_dict[60] * 60)
print(cycle_dict[100] * 100)
print(cycle_dict[140] * 140)
print(cycle_dict[180] * 180)
print(cycle_dict[220] * 220)

print(cycle_dict[20] * 20 + cycle_dict[60] * 60 + cycle_dict[100] * 100 + cycle_dict[140] * 140 + cycle_dict[180] * 180 + cycle_dict[220] * 220)