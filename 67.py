import math

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.__tracks = []

    def add_track(self, tr):
        self.__tracks.append(tr)

    def get_tracks(self):
        return tuple(self.__tracks)

    def __len__(self):
        current_x, current_y = self.start_x, self.start_y
        total_length = 0.0

        for track_line in self.__tracks:
            dx = track_line.to_x - current_x
            dy = track_line.to_y - current_y
            segment_length = math.sqrt(dx ** 2 + dy ** 2)
            total_length += segment_length
            current_x, current_y = track_line.to_x, track_line.to_y

        return int(total_length)

    def __eq__(self, other):
        return len(self) == len(other)

    def __ne__(self, other):
        return len(self) != len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
