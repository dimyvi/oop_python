class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}:{self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if type(new_width) is int and new_width in range(0, 10000):
            self.__width = new_width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if type(new_height) is int and new_height in range(0, 10000):
            self.__height = new_height
            self.show()
