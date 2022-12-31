import numpy as np
from Me import Me
class Landscape():
    def __init__(self, input_array):
        self.elevation_array = input_array
        self.path_array = np.full(self.elevation_array.shape, 0)
        self.current_level_curve = self.isolate_level_curve(1, 3)
        self.start = self.find_start()
        self.end = self.find_end()
        self.me = Me(self.start[0], self.start[1], self.elevation_array[self.start[1]][self.start[0]])
        self.path_array[self.me.get_coords()] = 1
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
                    self.start = (j, i)
        return self.start
    def find_end(self):
        for i in range(len(self.elevation_array)):
            for j in range(len(self.elevation_array[i])):
                if self.elevation_array[i][j] == 27:
                    self.end = (j, i)
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
                return True
            return False
        elif direction == "left":
            if self.me.x - 1 >= 0 and self.elevation_array[self.me.y][self.me.x - 1] <= self.me.elevation + 1:
                self.me.move_left(self.elevation_array)
                return True
            return False
        elif direction == "up":
            if self.me.y - 1 >= 0 and self.elevation_array[self.me.y - 1][self.me.x] <= self.me.elevation + 1:
                self.me.move_up(self.elevation_array)
                return True
            return False
        elif direction == "down":
            if self.me.y + 1 < len(self.elevation_array) and self.elevation_array[self.me.y + 1][self.me.x] <= self.me.elevation + 1:
                self.me.move_down(self.elevation_array)
                return True
            return False
    def find_path(self):
        return None