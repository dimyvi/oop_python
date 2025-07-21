class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.tail is None:
            return

        if self.tail.get_prev() is None:
            self.head = None
            self.tail = None
        else:
            new_tail = self.tail.get_prev()
            new_tail.set_next(None)
            self.tail = new_tail

    def get_data(self):
        data = []
        current = self.head
        while current is not None:
            data.append(current.get_data())
            current = current.get_next()
        return data