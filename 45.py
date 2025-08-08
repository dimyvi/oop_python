import time

class Mechanical:
    def init(self, date):
        self.date = date

    def setattr(self, name, value):
        if name == 'date' and 'date' in self.dict:
            return
        super().setattr(name, value)

class Aragon:
    def init(self, date):
        self.date = date

    def setattr(self, name, value):
        if name == 'date' and 'date' in self.dict:
            return
        super().setattr(name, value)

class Calcium:
    def init(self, date):
        self.date = date

    def setattr(self, name, value):
        if name == 'date' and 'date' in self.dict:
            return
        super().setattr(name, value)

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def init(self):
        self.slots = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if slot_num not in self.slots:
            return

        current_filter = self.slots[slot_num]
        if current_filter is not None:
            return

        if (slot_num == 1 and isinstance(filter, Mechanical)) or \
           (slot_num == 2 and isinstance(filter, Aragon)) or \
           (slot_num == 3 and isinstance(filter, Calcium)):
            self.slots[slot_num] = filter

    def remove_filter(self, slot_num):
        if slot_num in self.slots:
            self.slots[slot_num] = None

    def get_filters(self):
        return tuple(self.slots[i] for i in sorted(self.slots.keys()))

    def water_on(self):
        filters = self.get_filters()
        if None in filters:
            return False

        current_time = time.time()
        for f in filters:
            if not (0 <= (current_time - f.date) <= self.MAX_DATE_FILTER):
                return False

        return True