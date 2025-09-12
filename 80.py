class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self._fields = list(kwargs.keys())

    def __getitem__(self, index):
        if not isinstance(index, int) or not (0 <= index < len(self._fields)):
            raise IndexError('неверный индекс поля')
        field_name = self._fields[index]
        return getattr(self, field_name)

    def __setitem__(self, index, value):
        if not isinstance(index, int) or not (0 <= index < len(self._fields)):
            raise IndexError('неверный индекс поля')
        field_name = self._fields[index]
        setattr(self, field_name, value)