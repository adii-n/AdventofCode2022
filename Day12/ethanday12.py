import numpy as np
from Me import Me
from Landscape import Landscape
from astar import Astar

text = open("ethan12.txt").read().splitlines()
# text = open("sample12.txt").read().splitlines()
elevation_array = []
for line in text:
    array_to_append = []
    for char in line:
        if char == 'S':
            array_to_append.append(0)
        elif char == 'E':
            array_to_append.append(27)
        else:
            array_to_append.append(ord(char) - ord('a') + 1)
    elevation_array.append(array_to_append)
numpy_elevation_array = np.array(elevation_array)


landscape = Landscape(numpy_elevation_array)
# print(landscape)
# landscape.me_move("right")
# print(landscape)
# path = landscape.find_path()
# print(path)
# astar = Astar()
path = landscape.find_path()
print(path)