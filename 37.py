class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        if 0 <= indx < len(self.__things):
            self.__things.pop(indx)

    def get_total_weight(self):
        return sum(thing.weight for thing in self.__things)


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
