class Clock:
    def __init__(self, time):
        self.__time = 0
        self.set_time(time)

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    def __check_time(self, tm):
        if isinstance(tm, int) and 0 <= tm < 100000:
            return True
        return False

clock = Clock(4530)
