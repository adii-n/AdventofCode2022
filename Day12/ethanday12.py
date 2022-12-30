import numpy as np
elevation_array = np.loadtxt("ethan12.txt", dtype=str)
print(elevation_array)

# Find the coordinates of S and E
for i in range(len(elevation_array)):
    for j in range(len(elevation_array[i])):
        if elevation_array[i][j] == "S":
            start = (i, j)
        if elevation_array[i][j] == "E":
            end = (i, j)

print(start, end)

# Move from S to E while only moving up one elevation at a time and only moving in the cardinal directions and keep track of the number of steps taken
# Use a queue to keep track of the possible paths
# Use a set to keep track of the visited nodes
# Use a dictionary to keep track of the path taken to get to each node
# Use a dictionary to keep track of the distance from the start to each node
from collections import deque
queue = deque()
visited = set()
path = {}
distance = {}
queue.append(start)
visited.add(start)
distance[start] = 0
while queue:
    current = queue.popleft()
    if current == end:
        break
    for neighbor in [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]:
        if neighbor[0] < 0 or neighbor[0] >= len(elevation_array) or neighbor[1] < 0 or neighbor[1] >= len(elevation_array[0]):
            continue
        if neighbor in visited:
            continue
        if elevation_array[neighbor[0]][neighbor[1]] == "#":
            continue
        if elevation_array[neighbor[0]][neighbor[1]] == "E":
            distance[neighbor] = distance[current] + 1
            path[neighbor] = current
            break
        if elevation_array[neighbor[0]][neighbor[1]] == ".":
            if elevation_array[current[0]][current[1]] == "." or int(elevation_array[neighbor[0]][neighbor[1]]) == int(elevation_array[current[0]][current[1]]) + 1:
                distance[neighbor] = distance[current] + 1
                path[neighbor] = current
                queue.append(neighbor)
                visited.add(neighbor)