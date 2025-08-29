import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        return (self.name.lower() == other.name.lower() and
                self.weight == other.weight and
                self.price == other.price)

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))


lst_in = list(map(str.strip, sys.stdin.readlines()))

shop_items = {}

for line in lst_in:
    if ':' in line:
        name_part, numbers_part = line.split(':', 1)
        name = name_part.strip()

        numbers = numbers_part.strip().split()
        if len(numbers) >= 2:
            weight = float(numbers[0])
            price = float(numbers[1])

            item = ShopItem(name, weight, price)

            if item in shop_items:
                shop_items[item][1] += 1
            else:
                shop_items[item] = [item, 1]