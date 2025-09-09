class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __check_dimensions(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        if isinstance(other, Vector):
            self.__check_dimensions(other)
            return Vector(*[a + b for a, b in zip(self.coords, other.coords)])
        return Vector(*[a + other for a in self.coords])

    def __sub__(self, other):
        if isinstance(other, Vector):
            self.__check_dimensions(other)
            return Vector(*[a - b for a, b in zip(self.coords, other.coords)])
        return Vector(*[a - other for a in self.coords])

    def __mul__(self, other):
        if isinstance(other, Vector):
            self.__check_dimensions(other)
            return Vector(*[a * b for a, b in zip(self.coords, other.coords)])
        return Vector(*[a * other for a in self.coords])

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.__check_dimensions(other)
            self.coords = [a + b for a, b in zip(self.coords, other.coords)]
        else:
            self.coords = [a + other for a in self.coords]
        return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.__check_dimensions(other)
            self.coords = [a - b for a, b in zip(self.coords, other.coords)]
        else:
            self.coords = [a - other for a in self.coords]
        return self

    def __eq__(self, other):
        if not isinstance(other, Vector) or len(self.coords) != len(other.coords):
            return False
        return all(a == b for a, b in zip(self.coords, other.coords))

    def __ne__(self, other):
        return not self.__eq__(other)