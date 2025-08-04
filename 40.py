class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    __id_counter = 1

    def __init__(self, name, weight, price):
        self.id = self.__generate_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __generate_id(self):
        id = Product.__id_counter
        Product.__id_counter += 1
        return id

    def __setattr__(self, name, value):
        if name == 'id' and isinstance(value, int) and value > 0:
            super().__setattr__(name, value)
        elif name == 'name' and isinstance(value, str):
            super().__setattr__(name, value)
        elif name in ('weight', 'price') and isinstance(value, (int, float)) and value > 0:
            super().__setattr__(name, value)
        else:
            if name in ('id', 'name', 'weight', 'price'):
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(name)