class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int,float))):
            return 1
        if not (self.a <= 0 and self.b <= 0 and self.c <= 0):
            return False
        if self.a + self.b > self.c and self.c + self.b > self.a and self.a + self.c > self.b:
            return 2
        return True


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
ans = tr.is_triangle()
print(ans)
