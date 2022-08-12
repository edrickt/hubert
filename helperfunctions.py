import requests
import json

class User:
    def __init__(self, data):
        User.uuid = data["id"]
        User.name = data["name"]

def WhitelistUser(user):
    request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{user}?at=<timestamp>")
    if request.status_code == 200:
        userInformation = request.json()
        newUser = User(userInformation)

        with open("../whitelist.json") as fp:
            listObj = json.load(fp)
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
