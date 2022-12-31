import numpy as np
from Me import Me
from Node import Node
class Landscape():
    def __init__(self, input_array):
        self.elevation_array = input_array
        self.path_array = np.full(self.elevation_array.shape, 0)
        self.current_level_curve = self.isolate_level_curve(1, 3)
        self.start = Node(None, self.find_start())
        self.end = Node(None, self.find_end())
        self.me = Me(self.start.position[0], self.start.position[1], self.elevation_array[self.start.position[0]][self.start.position[1]])
        self.path_array[self.me.get_coords()] = 1
        self.open_list = []
        self.closed_list = []
        self.open_list.append(self.start)
    
    def print_array(self, array):
        for i in range(len(array)):
            for j in range(len(array[i])):
                print(f"{array[i][j]:02d}", end=" ")
            print()
    def __str__(self):
        print("Elevation Array:")
        self.print_array(self.elevation_array)
        print()
        print("Path Array:")
        self.print_array(self.path_array)
        print()
        print("Current Level Curve:")
        self.print_array(self.current_level_curve)
        print()
        print(f"Me: {self.me}")
        return ""
    
    def find_start(self):
        for i in range(len(self.elevation_array)):
            for j in range(len(self.elevation_array[i])):
                if self.elevation_array[i][j] == 0:
                    self.start = (i, j)
        return self.start
    
    def find_end(self):
        for i in range(len(self.elevation_array)):
            for j in range(len(self.elevation_array[i])):
                if self.elevation_array[i][j] == 27:
                    self.end = (i, j)
        return self.end
    
    def isolate_level_curve(self, low_elev, high_elev):
        if low_elev == 1:
            low_elev = 0
        level_curve = np.copy(self.elevation_array)
        for i in range(len(level_curve)):
            for j in range(len(level_curve[i])):
                if not (level_curve[i][j] >= low_elev and level_curve[i][j] <= high_elev):
                    level_curve[i][j] = -1
        return level_curve
    
    def me_move(self, direction):
        if direction == "right":
            if self.me.x + 1 < len(self.elevation_array[self.me.y]) and self.elevation_array[self.me.y][self.me.x + 1] <= self.me.elevation + 1:
                self.me.move_right(self.elevation_array)
                self.path_array[self.me.get_coords()] = 1
                self.path.append("right")
                return True
            return False
        elif direction == "left":
            if self.me.x - 1 >= 0 and self.elevation_array[self.me.y][self.me.x - 1] <= self.me.elevation + 1:
                self.me.move_left(self.elevation_array)
                self.path_array[self.me.get_coords()] = 1
                self.path.append("left")
                return True
            return False
        elif direction == "up":
            if self.me.y - 1 >= 0 and self.elevation_array[self.me.y - 1][self.me.x] <= self.me.elevation + 1:
                self.me.move_up(self.elevation_array)
                self.path_array[self.me.get_coords()] = 1
                self.path.append("up")
                return True
            return False
        elif direction == "down":
            if self.me.y + 1 < len(self.elevation_array) and self.elevation_array[self.me.y + 1][self.me.x] <= self.me.elevation + 1:
                self.me.move_down(self.elevation_array)
                self.path_array[self.me.get_coords()] = 1
                self.path.append("down")
                return True
            return False
        return False

    def find_path(self):
        while len(self.open_list) > 0:
            current_node = self.open_list[0]
            current_index = 0
            for index, item in enumerate(self.open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
            
            self.open_list.pop(current_index)
            self.closed_list.append(current_node)

            if current_node == self.end:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]
            
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                node_position = current_node.position[0] + new_position[0], current_node.position[1] + new_position[1]

                if node_position[0] > (len(self.elevation_array) - 1) or node_position[0] < 0 or node_position[1] > (len(self.elevation_array[node_position[0]]) -1) or node_position[1] < 0:
                    continue

                if self.elevation_array[node_position[0]][node_position[1]] > self.elevation_array[current_node.position[0]][current_node.position[1]] + 1:
                    continue

                new_node = Node(current_node, node_position)
                children.append(new_node)
            
            for child in children:
                for closed_child in self.closed_list:
                    if child == closed_child:
                        continue
                child.g = current_node.g + 1
                child.h = ((child.position[0] - self.end.position[0]) ** 2) + ((child.position[1] - self.end.position[1]) ** 2)
                child.f = child.g + child.h

                for open_node in self.open_list:
                    if child == open_node and child.g > open_node.g:
                        continue
                
                self.open_list.append(child)