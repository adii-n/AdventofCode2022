CUBE_SIZE = 1

class Cube:
    GLOBAL_MAX_X = 0
    GLOBAL_MAX_Y = 0
    GLOBAL_MAX_Z = 0    
    def __init__(self, x, y, z, kind):
        self.x = x
        self.y = y
        self.z = z
        self.kind = kind
        if x > Cube.GLOBAL_MAX_X:
            Cube.GLOBAL_MAX_X = x
        if y > Cube.GLOBAL_MAX_Y:
            Cube.GLOBAL_MAX_Y = y
        if z > Cube.GLOBAL_MAX_Z:
            Cube.GLOBAL_MAX_Z = z
    def __str__(self):
        return "Cube(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " +str(self.kind) +")"
    def is_adjacent(self, other_cube):
        x_diff = abs(self.x - other_cube.x)
        y_diff = abs(self.y - other_cube.y)
        z_diff = abs(self.z - other_cube.z)
        total_diff = x_diff + y_diff + z_diff
        if total_diff == CUBE_SIZE:
            return True
        return False
    def __eq__(self, other_cube):
        if self.x == other_cube.x and self.y == other_cube.y and self.z == other_cube.z and self.kind == other_cube.kind:
            return True
        return False
    def __hash__(self):
        return hash((self.x, self.y, self.z, self.kind))
text = (open("ethan18.txt")).read()
# text = (open("ethanSample.txt")).read()
text = text.split("\n")
cubes = []
for cube in text:
    cube = cube.split(",")
    cubes.append(Cube(int(cube[0]), int(cube[1]), int(cube[2]), "Lava"))
cubes = list(set(cubes))
adjacentCount = 0
for cube in cubes:
    for other_cube in cubes:
        if cube.is_adjacent(other_cube):
            adjacentCount += 1
cubeCount = len(cubes)
cubeSurfaceArea = cubeCount * 6 * (CUBE_SIZE**2)
adjacentSurfaceArea = adjacentCount * (CUBE_SIZE**2)
totalSurfaceArea = cubeSurfaceArea - adjacentSurfaceArea
print("Total Surface Area from Part 1: " + str(totalSurfaceArea))

# Mapping points to local min/max
points_dict = {}
def build_points_dict():
    for currentX in range(0, Cube.GLOBAL_MAX_X+1):
        for currentY in range(0, Cube.GLOBAL_MAX_Y+1):
            filteredCubes = list(filter(lambda cube: cube.x == currentX and cube.y == currentY, cubes))
            # print("x: {}, y: {}, cubes:".format(x, y))
            # print(*filteredCubes)
            filteredCubes.sort(key=lambda cube: cube.z)
            if len(filteredCubes) <= 1:
                local_min_z = -1
                local_max_z = -1
            else:
                local_min_z = filteredCubes[0].z
                local_max_z = filteredCubes[-1].z
            for currentZ in range(0, Cube.GLOBAL_MAX_Z+1):
                point = "({},{},{})".format(currentX, currentY, currentZ)
                points_dict[point] = {"local_min_z": local_min_z, "local_max_z": local_max_z}
    for currentX in range(0, Cube.GLOBAL_MAX_X+1):
        for currentZ in range(0, Cube.GLOBAL_MAX_Z+1):
            filteredCubes = list(filter(lambda cube: cube.x == currentX and cube.z == currentZ, cubes))
            filteredCubes.sort(key=lambda cube: cube.y)
            if len(filteredCubes) <= 1:
                local_min_y = -1
                local_max_y = -1
            else:
                local_min_y = filteredCubes[0].y
                local_max_y = filteredCubes[-1].y
            for currentY in range(0, Cube.GLOBAL_MAX_Y+1):
                point = "({},{},{})".format(currentX, currentY, currentZ)
                # points_dict[point] = {"local_min_y": local_min_y, "local_max_y": local_max_y}
                points_dict[point]["local_min_y"] = local_min_y
                points_dict[point]["local_max_y"] = local_max_y
    for currentY in range(0, Cube.GLOBAL_MAX_Y+1):
        for currentZ in range(0, Cube.GLOBAL_MAX_Z+1):
            filteredCubes = list(filter(lambda cube: cube.y == currentY and cube.z == currentZ, cubes))
            filteredCubes.sort(key=lambda cube: cube.x)
            if len(filteredCubes) <= 1:
                local_min_x = -1
                local_max_x = -1
            else:
                local_min_x = filteredCubes[0].x
                local_max_x = filteredCubes[-1].x
            for currentX in range(0, Cube.GLOBAL_MAX_X+1):
                point = "({},{},{})".format(currentX, currentY, currentZ)
                # points_dict[point] = {"local_min_x": local_min_x, "local_max_x": local_max_x}
                points_dict[point]["local_min_x"] = local_min_x
                points_dict[point]["local_max_x"] = local_max_x

build_points_dict()

# Identify Holes
holes = []
def build_holes():
    for x in range(0, Cube.GLOBAL_MAX_X+1):
        for y in range(0, Cube.GLOBAL_MAX_Y+1):
            for z in range(0, Cube.GLOBAL_MAX_Z+1):
                point = "({},{},{})".format(x, y, z)
                # if point not in points_dict:
                #     points_dict[point] = {"local_min_x": -1, "local_max_x": -1, "local_min_y": -1, "local_max_y": -1, "local_min_z": -1, "local_max_z": -1}
                if x in range(points_dict[point]["local_min_x"], points_dict[point]["local_max_x"]+1) and y in range(points_dict[point]["local_min_y"], points_dict[point]["local_max_y"]+1) and z in range(points_dict[point]["local_min_z"], points_dict[point]["local_max_z"]+1):
                    if points_dict[point]["local_min_x"] != -1 and points_dict[point]["local_max_x"] != -1 and points_dict[point]["local_min_y"] != -1 and points_dict[point]["local_max_y"] != -1 and points_dict[point]["local_min_z"] != -1 and points_dict[point]["local_max_z"] != -1:
                        if Cube(x,y,z,"Lava") not in cubes:
                            holes.append(Cube(x,y,z,"Hole"))
build_holes()
print("Number of holes: " + str(len(holes)))
holeAdjacencyCount = 0
for hole in holes:
    for cube in cubes:
        if hole.is_adjacent(cube):
            holeAdjacencyCount += 1
print(holeAdjacencyCount)
print("Total Exterior Surface Area from Part 2: " + str(totalSurfaceArea - (holeAdjacencyCount * (CUBE_SIZE**2))))