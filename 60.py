from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], int) and args[0] > 1:
            self.vector = [0.0] * args[0]
        else:
            self.vector = list(args)

    def set_coords(self, *args):
        for i in range(min(len(args), len(self.vector))):
            self.vector[i] = args[i]

    def get_coords(self):
        return tuple(self.vector)

    def __len__(self):
        return len(self.vector)

    def __abs__(self):
        return sqrt(sum(x ** 2 for x in self.vector))
