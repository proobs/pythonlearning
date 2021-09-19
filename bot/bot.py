# Author: proobs
import discord
import json

from discord.ext import commands

# Honestly IDK if this is even the right way to go about things but whatever
token, data, prefix = "", "", ""

bot = commands.Bot(command_prefix="%s" % cmd_prefix)

@bot.command()
async def printmsg(ctx):
    await ctx.send('Done')

client = Role()
client.run(token)

with open('config.json') as json_file:
    data = json.load(json_file)
