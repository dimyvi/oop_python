import sys

class ListObject:
    def __init__(self, data):
        self.next_obj = None
        self.data = data

    def link(self, obj):
        self.next_obj = obj

lst_in = list(map(str.strip, sys.stdin.readlines()))

if lst_in:
    head_obj = ListObject(lst_in[0])
    current = head_obj
    for data in lst_in[1:]:
        new_obj = ListObject(data)
        current.link(new_obj)
        current = new_obj
