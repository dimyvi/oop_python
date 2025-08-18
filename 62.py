class Recipe:
    def __init__(self, *args):
        self.ls = list(args)

    def add_ingredient(self, ing):
        self.ls.append(ing)

    def remove_ingredient(self, ing):
        self.ls.remove(ing)

    def get_ingredients(self):
        return tuple(self.ls)

    def __len__(self):
        return len(self.ls)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"