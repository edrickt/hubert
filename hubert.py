import os
import discord
from hubertrcon import HubertRCON

file = open("token.txt", "r")
TOKEN = file.read()
client = discord.Client(intents=discord.Intents.all())
hr = HubertRCON("192.168.1.60", 25575, "password")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    content = message.content.split()

    if content[0] == ("!!hubie"):
        if content[1] == ("whitelist"):
            command = content[1]
            action = content[2]
            if action == "add":
                response = hr.run(f"{command} {action} {content[3]}")
            elif action == "remove":
                response = hr.run(f"{command} {action} {content[3]}")
            elif action == "list":
                response = hr.run(f"{command} {action}")
            print(response)
            await message.channel.send(f"{response}")

client.run(TOKEN)