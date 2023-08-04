from rcon.source import Client

class HubertRCON:
    def __init__(self, ip, port, password):
        self.ip = ip
        self.port = port
        self.password = password

    def run(self, command, *args):
        with Client(self.ip, self.port, passwd=self.password) as client:
            response = client.run(command, *args)
            return response
