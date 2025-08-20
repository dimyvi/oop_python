class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + (other.money if isinstance(other, Item) else other)

    def __radd__(self, other):
        return other + self.money

class Budget:
    def __init__(self):
        self.ls = []

    def add_item(self, it):
        self.ls.append(it)

    def remove_item(self, indx):
        del self.ls[indx]

    def get_items(self):
        return self.ls