import discord
from discord.ext import commands
import datetime


prefix = "t!"
token = "OTQ4NDgyNTE2MDM2MjI3MDky.Yh8dLQ.mc1c4rwjvQGrZ1b6U4KWK7htgB0"

client = commands.Bot(command_prefix=prefix)



@client.event
async def on_ready():
    print("discord.py version" + discord.__version__)


client.run(token)
