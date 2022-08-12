from helperfunctions import *
import discord

infoFile = open("../info.txt", "r")
TOKEN = infoFile.readline()
client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

@client.event
async def on_message(message):
    content = message.content

    if content.startswith("!!whitelist add"):
        user = content.replace("!!whitelist add ", "")
        userAdded = WhitelistUser(user)
        if userAdded:
            await message.channel.send("User successfully whitelisted")
        else:
            await message.channel.send("User not found")
        return

client.run(TOKEN)
