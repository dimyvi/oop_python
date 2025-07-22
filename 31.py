class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if type(new_x) in (int, float) and self.MIN_COORD <= new_x <= self.MAX_COORD:
            self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if type(new_y) in (int, float) and self.MIN_COORD <= new_y <= self.MAX_COORD:
            self.__y = new_y

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y
