class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position
    def __str__(self):
        print(f"Position: {self.position}, G: {self.g}, H: {self.h}, F: {self.f}")