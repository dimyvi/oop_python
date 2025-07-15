class SingletonFive:
    _instances = []
    _count = 0

    def __new__(cls, *args, **kwargs):
        if len(cls._instances) < 5:
            obj = super().__new__(cls)
            cls._instances.append(obj)
            return obj
        return cls._instances[4]

    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
