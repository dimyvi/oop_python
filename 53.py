class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        input_str = self.func()
        return list(map(int, input_str.split()))


input_dg = InputDigits(input)
res = input_dg()