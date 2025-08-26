class Box:
    def __init__(self):
        self.ls = []

    def add_thing(self, obj):
        pass

    def get_things(self):
        pass

    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass

    def __ne__(self, other):
        return not (self.name == other.name and self.mass == other.mass)

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass

    def __ne__(self, other):
        return not (self.name == other.name and self.mass == other.mass)