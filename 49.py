from curses.ascii import isdigit


class DigitRetrieve:
    def __init__(self, string=''):
        self.string = string

    def __call__(self, string):
        if string.isdigit() or string[1:].isdigit() and string.find('.') == -1:
            return int(string)
        return None

dg = DigitRetrieve()
d1 = dg("123")
d2 = dg("45.54")
d3 = dg("-56")
d4 = dg("12fg")
d5 = dg("abc")
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))

print(digits)
