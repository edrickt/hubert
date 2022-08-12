import os
import discord

infoFile = open("../info.txt", "r")
TOKEN = infoFile.readline()
client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

client.run(TOKEN)