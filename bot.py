import os
import discord

import query

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='//', help_command=None)

@bot.event
async def on_ready():
    print('Bot running')

@bot.event
async def on_message(message):
    if message.content.lower() == 'hello':
        await message.channel.send(f'hello {message.author}, try //help for help with the bot')
    await bot.process_commands(message)

@bot.command(name="help")
async def help(ctx, *arg):
    if len(arg) == 0:
        await ctx.send("""```
Hi, I am the Minecraft Discord Bot!\n
My command prefix is //\n
Available commands:
help        : display this help message, use //help <command> to see help for a command
server <ip> : get generic server information
online <ip> : see whether a server is online
players <ip> : get the players that are online
```""")
    elif len(arg) == 1:
        command = arg[0]
        if command == "server":
            await ctx.send("```//server <ip>: call this command to get all information from Anders G. Jørgensen's MCSRVSTATUS API. <ip> is a required argument and is the ip or domain name of the server you want to query. For example: //server mineplex.com```")
        elif command == "online":
            await ctx.send("```//online <ip>: call this command to see whether a server is online. <ip> is a required argument and is the ip or domain name of the server you want to query. For example: //online mineplex.com```")
        else:
            await ctx.send("Command doesn't have a help yet")

@bot.command(name='server')
async def server(ctx, ip):
    serverInfo = query.get(ip)
    print(serverInfo)
    # await ctx.send(file=discord.File("icon.png"))
    await ctx.send("```" + serverInfo + "```")

@bot.command(name="online")
async def online(ctx, ip):
    isOnline = query.online(ip)
    if isOnline:
        await ctx.send("```" + ip + " is Online! :D ```")
    else:
        await ctx.send("```" + ip + " is Offline! :( ```")

@bot.command(name="players")
async def players(ctx, ip):
    playersArr = query.players(ip)
    await ctx.send("Players online: " + str(playersArr["online"]))
    if "list" in playersArr:
        await ctx.send("```" + str(playersArr["list"]) + "```")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Sorry, that command went wrong, here's the message:\n```" + str(error) + "```")

bot.run(TOKEN)