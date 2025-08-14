class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail is None:  # Если список пуст
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        current = self.head
        count = 0
        while current and count != indx:
            current = current.next
            count += 1

        if current is None:
            return

        if current.prev:
            current.prev.next = current.next
        else:  # Удаляем первый элемент
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:  # Удаляем последний элемент
            self.tail = current.prev

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __call__(self, indx):
        current = self.head
        count = 0
        while current and count != indx:
            current = current.next
            count += 1

        if current is None:
            return ""
        return current.data