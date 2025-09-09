import sys

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return True if self.score > 0 else False

lst_in = list(map(str.strip, sys.stdin.readlines()))

ls = [Player(i[0], i[1], int(i.split('; ')[2])) for i in lst_in]

players_filtered = list(filter(lambda x: bool(x), ls))







