import numpy as np
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

print(cycle_dict[20] * 20 + cycle_dict[60] * 60 + cycle_dict[100] * 100 + cycle_dict[140] * 140 + cycle_dict[180] * 180 + cycle_dict[220] * 220)

cycle_array = np.zeros((6, 40), dtype='int')

print(cycle_array)

def get_cycle_coords(cycle):
    # if cycle % 40 == 0:
    #     return (cycle // 40 - 1, 39)
    return (cycle // 40, (cycle - 1) % 40)

def get_sprite_pixels(cycle):
    x = cycle_dict[cycle]
    return (x - 1, x, x + 1)

for cycle in range(1, 241):
# for cycle in range(1, 3):
    current_cycle_coords = get_cycle_coords(cycle)
    current_sprite_pixels = get_sprite_pixels(cycle)
    if (current_cycle_coords[1]) == current_sprite_pixels[0] or (current_cycle_coords[1]) == current_sprite_pixels[1] or (current_cycle_coords[1]) == current_sprite_pixels[2]:
        cycle_array[current_cycle_coords[0], current_cycle_coords[1]] = 1

print("New array:")
print(cycle_array)
for line in cycle_array:
    for element in line:
        if element == 0:
            print(" ", end=" ")
        else:
            print('#', end=" ")
    print()