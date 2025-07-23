class PhoneBook:
    def __init__(self):
        self.ls = []

    def add_phone(self, phone):
            self.ls.append(phone)

    def remove_phone(self, indx):
        del self.ls[indx]

    def get_phone_list(self):
        return self.ls

class PhoneNumber:
    def __init__(self, number, fio):
        if isinstance(number, int) and len(str(number)) == 11:
            self.number = number
        if isinstance(fio, str):
            self.fio = fio


