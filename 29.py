class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, st):
        if type(st) is str and 2 <= len(st) <= 100:
            self.__model = st


