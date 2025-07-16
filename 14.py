class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def clone(self):
        return Point(self.x, self.y)

pt = Point(3, 5)
pt_clone = pt.clone()