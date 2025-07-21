class Point:
    def __init__(self, x, y):
        self.__x, self.__y = x, y

    def get_coords(self):
        return (self.__x, self.__y)


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = (args[0], args[1])
            self.__ep = (args[2], args[3])

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        coords = self.get_coords()
        print(f"рямоугольник с координатами: {coords[0], coords[1]} {coords[2], coords[3]}")

rect = Rectangle(0, 0, 20, 34)