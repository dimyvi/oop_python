class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def mass(self):
        return self.ro * self.volume

    def __eq__(self, other):
        return self.mass() == other

    def __lt__(self, other):
        return self.mass() < other

    def __gt__(self, other):
        return self.mass() > other
