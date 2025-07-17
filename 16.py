class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2025-birth_year)
p1 = Person('efr', 23)
p2 = Person.from_birth_year('jdcnd', 1968)

print(p1.name, p1.age)
print(p2.name, p2.age)