class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = max(0, int(hours))
        self.minutes = max(0, int(minutes))
        self.seconds = max(0, int(seconds))

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        delta = max(0, self.clock1.get_time() - self.clock2.get_time())
        hours = delta // 3600
        minutes = (delta % 3600) // 60
        seconds = delta % 60
        return f"{hours:02d}: {minutes:02d}: {seconds:02d}"

    def __len__(self):
        return max(0, self.clock1.get_time() - self.clock2.get_time())