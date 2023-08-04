from rcon.source import rcon

class HubertRCON:
    def __init__(self, ip, port, password):
        self.ip = ip
        self.port = port
        self.password = password

    async def run(self, command, *args):        
        response = await rcon(command, *args, host=self.ip, port=self.port, passwd=self.password)
        return response
