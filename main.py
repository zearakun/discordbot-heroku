import discord
from discord.ext import discord
import datetime


prefix = "プレフィックス"
token = "トークン"

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    change_status.start()
    print("discord.py version" + discord.__version__)



@client.command()
async def ping(ctx):
    embed = discord.Embed(title=f"pong!:ping_pong:", color=0x979c9f)
    embed.add_field(name="ping",
                    value=f"{client.latency*1000}ms",
                    inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.reply(embed=embed)


client.run(token)
