class AppStore:
    apps = []
    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        self.apps.remove(app)

    @staticmethod
    def block_application(app):
        app.blocked = True

    def total_apps(self):
        return len(self.apps)

class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.total_apps())
store.remove_application(app_youtube)