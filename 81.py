class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise ValueError('должно быть целое число')
        self.__value = val

class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.__array = [cell() for _ in range(max_length)]

    def __check_index(self, index):
        if not isinstance(index, int):
            raise IndexError('неверный индекс для доступа к элементам массива')
        if index < 0 or index >= self.__max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, index):
        self.__check_index(index)
        return self.__array[index].value

    def __setitem__(self, index, value):
        self.__check_index(index)
        self.__array[index].value = value

    def __str__(self):
        return ' '.join(str(item.value) for item in self.__array)

