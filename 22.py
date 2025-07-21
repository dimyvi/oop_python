class Server:
    def __init__(self, ip):
        self.ip = ip
        self.buffer = []

    def send_data(self, data):
        Router().buffer.append(data)

    def get_data(self):
        received_data = self.buffer.copy()
        self.buffer.clear()
        return received_data

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.ip] = server

    def unlink(self, server):
        if server.ip in self.servers:
            del self.servers[server.ip]

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data.data)
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

