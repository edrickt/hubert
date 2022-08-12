import requests
import json
from mcstatus import JavaServer

class User:
    def __init__(self, data):
        self.uuid = data["id"]
        self.name = data["name"]

class Server:
    def __init__(self, server):
        self.playersonline = server.status.players.online
        self.ping = server.status.latency


def WhitelistUser(user):
    request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{user}?at=<timestamp>")
    if request.status_code == 200:
        userInformation = request.json()
        newUser = User(userInformation)

        with open("../whitelist.json") as fp:
            listObj = json.load(fp)

        for idx, user in enumerate(listObj):
            if newUser.name.lower() == user["name"].lower():
                return False

        listObj.append({
            "uuid" : f"{newUser.uuid}",
            "name" : f"{newUser.name}"
        })
        with open("../whitelist.json", 'w') as json_file:
            json.dump(listObj, json_file,
                      indent=4,
                      separators=(',', ': '))

        return True
    else:
        return False

def RemoveWhitelist(user):
        removedUser = user

        with open("../whitelist.json") as fp:
            listObj = json.load(fp)
        for idx, user in enumerate(listObj):
            if removedUser.lower() == user["name"].lower():
                listObj.pop(idx)
                with open("../whitelist.json", "w") as json_file:
                    json.dump(listObj, json_file,
                              indent=4,
                              separators=(',', ': '))
                return True
        return False

class Server():
    def __init__(self, connection):
        self.playersonline = connection.status().players.online
        self.latency = connection.status().latency
        self.playerslist = connection.query().players.names

def GetServerStatus():
    connection = JavaServer.lookup("localhost:25565")
    server = Server(connection)
    print(server)
    return server
