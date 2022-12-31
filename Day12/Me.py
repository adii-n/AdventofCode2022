class Me():
    def __init__(self, x, y, elevation):
        self.x = x
        self.y = y
        self.elevation = elevation
    def __str__(self):
        return f"({self.x}, {self.y}, {self.elevation})"
    def get_coords(self):
        return (self.y, self.x)
    def move_right(self, elevation_array):
        self.x += 1
        self.elevation = elevation_array[self.y][self.x]
    def move_left(self, elevation_array):
        self.x -= 1
        self.elevation = elevation_array[self.y][self.x]
    def move_up(self, elevation_array):
        self.y -= 1
        self.elevation = elevation_array[self.y][self.x]
    def move_down(self, elevation_array):
        self.y += 1
        self.elevation = elevation_array[self.y][self.x]