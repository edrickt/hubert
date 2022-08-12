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

    if content.startswith("!!whitelist add "):
        user = content.replace("!!whitelist add ", "")
        userAdded = WhitelistUser(user)
        if userAdded:
            await message.channel.send("User successfully whitelisted")
        else:
            await message.channel.send("User not found or already whitelisted")
        return

    if content.startswith("!!whitelist remove "):
        user = content.replace("!!whitelist remove ", "")
        userRemoved = RemoveWhitelist(user)
        if userRemoved:
            await message.channel.send("User successfully removed from whitelist")
        else:
            await message.channel.send("User not found")
        return

    if content == "!!status":
        server = GetServerStatus()
        embedMsg = discord.Embed(title=server.motd)
        embedMsg.add_field(name="Number online: ", value=server.playersonline, inline=False)
        embedMsg.add_field(name="Latency: ", value=server.latency, inline=true)
        await message.channel.send(embed=embedMsg)

client.run(TOKEN)
