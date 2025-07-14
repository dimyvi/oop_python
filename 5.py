import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = [random.choice([Line, Rect, Ellipse])(1, 2, 3, 4) for _ in range(217)]
for i in elements:
    if isinstance(i, Line):
        i.sp = (0, 0)
        i.ep = (0, 0)
