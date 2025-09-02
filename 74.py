import sys


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = int(year)

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.author.lower() == other.author.lower()


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = []
for line in lst_in:
    name, author, year = line.split('; ')
    bs = BookStudy(name, author, year)
    lst_bs.append(bs)
unique_books = len(set(lst_bs))
