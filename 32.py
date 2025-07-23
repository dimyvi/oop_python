import math

class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PathLines:
    def __init__(self, *lines):
        self.lines = list(lines)

    def get_path(self):
        return self.lines

    def add_line(self, line):
        self.lines.append(line)

    def get_length(self):
        if not self.lines:
            return 0

        total_length = 0.0
        prev_x, prev_y = 0, 0

        for line in self.lines:
            dx = line.x - prev_x
            dy = line.y - prev_y
            segment_length = math.sqrt(dx ** 2 + dy ** 2)
            total_length += segment_length
            prev_x, prev_y = line.x, line.y
        return total_length
