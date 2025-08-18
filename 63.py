class PolyLine:
    def __init__(self, start_coord, *args):
        self.ls = [start_coord] + list(args)

    def add_coord(self, x, y):
        self.ls.append((x, y))

    def remove_coord(self, indx):
        self.ls.pop(indx)

    def get_coords(self):
        return self.ls