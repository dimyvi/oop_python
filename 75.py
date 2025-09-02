class Dimensions:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

s_inp = input().strip()

lst_dims = []
if s_inp:
    parts = s_inp.split(';')
    for part in parts:
        part = part.strip()
        if part:
            try:
                a, b, c = map(float, part.split())
                dim = Dimensions(a, b, c)
                lst_dims.append(dim)
            except ValueError as e:
                if str(e) == "габаритные размеры должны быть положительными числами":
                    raise

lst_dims.sort(key=lambda x: hash(x))