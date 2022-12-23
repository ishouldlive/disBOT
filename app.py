import discord
from discord.ext import commands

description = "just trying to create something"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description=description,
    intents=intents
)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user} (ID: {bot.user.id})")
    print("----------")

@bot.command()
async def add(ctx: commands.Context, left: int, right:int):
    """Adds 2 numbers toghether."""
    await ctx.send(str(left + right))

bot.run("TOKEN")