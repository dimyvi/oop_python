class Model:
    def __init__(self):
        self.dt = dict()

    def query(self, **kwargs):
        for key, value in kwargs.items():
            self.dt[key] = value

    def __str__(self):
        string = "Model: "
        for i in self.dt:
            string = string + f"{i} = {self.dt[i]}, "
        return string[:-2]


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)