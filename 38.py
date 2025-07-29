class Telecast:
    def __init__(self, uid, name, duration):
        self.__id = uid
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


class TVProgram:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for i, item in enumerate(self.items):
            if item.uid == indx:
                del self.items[i]
                break