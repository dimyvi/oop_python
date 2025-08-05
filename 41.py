class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if not key == 'title' and isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif not key in ('practices', 'duration') and isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, name):
        return False

    def __delattr__(self, name):
        if name in ('title', 'practices', 'duration'):
            raise AttributeError(f"Нельзя удалять атрибут {name}")
        object.__delattr__(self, name)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        if isinstance(lesson, LessonItem):
            self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.remove(self.lessons[indx])


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.remove(self.modules[indx])

