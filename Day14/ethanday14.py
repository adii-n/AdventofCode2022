import re
import numpy as np
text = open("ethan14.txt").read()

rock_line_regex = re.compile(r'(\d+),(\d+)')
rock_array = []


cave_array = np.zeros((10, 10))
print(cave_array)

def draw_rock(input_arr, input_list):
    for i in range(len(input_list) - 1):
        start = input_list[i]
        end = input_list[i + 1]
        if start[0] == end[0]:
            for j in range(int(start[1]), int(end[1]) + 1):
                input_arr[int(start[0])][j] = "-1"
        elif start[1] == end[1]:
            for j in range(int(start[0]), int(end[0]) + 1):
                input_arr[j][int(start[1])] = "-1"
        else:
            raise Exception("Not a straight line")

for line in text.splitlines():
    rock_coords_list = re.findall(rock_line_regex, line)
    rock_array.append(rock_coords_list)
    draw_rock(cave_array, rock_coords_list)

print(cave_array)