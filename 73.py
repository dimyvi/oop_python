import sys

class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}
        self._pk_counter = 1

    def write(self, record):
        if record in self.dict_db:
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = [record]

        record.pk = self._pk_counter
        self._pk_counter += 1

    def read(self, pk):
        for records in self.dict_db.values():
            for record in records:
                if record.pk == pk:
                    return record
        return None

class Record:
    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = None

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        if not isinstance(other, Record):
            return False
        return self.fio.lower() == other.fio.lower() and self.old == other.old



lst_in = list(map(str.strip, sys.stdin.readlines()))

db = DataBase('database.db')


for line in lst_in:
    if line:
        parts = line.split(';')
        if len(parts) >= 3:
            fio = parts[0].strip()
            descr = parts[1].strip()
            old = int(parts[2].strip())

            record = Record(fio, descr, old)
            db.write(record)