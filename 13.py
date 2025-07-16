TYPE_OS = 1

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    def __new__(cls, name):
        if TYPE_OS == 1:
            instance = super().__new__(DialogWindows)
        else:
            instance = super().__new__(DialogLinux)
        instance.name = name
        return instance

    def __init__(self, name):
        self.name = name