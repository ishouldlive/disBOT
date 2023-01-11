import requests
import json
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
@commands.cooldown(3, 5, commands.BucketType.default)
async def add(ctx: commands.Context, left: int, right: int):
    try:
        result = left + right
    except:
        await ctx.send("Error: both arguments should be integers")
    await ctx.send(result)


@bot.command()
@commands.cooldown(3, 5, commands.BucketType.default)
async def minus(ctx: commands.Context, left: int, right: int):
    try:
        result = left - right
    except:
        await ctx.send("Error: both arguments should be integers")
    await ctx.send(result)

@bot.command()
@commands.cooldown(3, 5, commands.BucketType.default)
async def weather(ctx : commands.Context, city_Name: str, state_Code: commands.BadArgument = "",country_Code: commands.BadArgument = ""):
    endpoint = "http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={appid}"
    api_key = "API_KEY"
    params = {
        "city": city_Name,
        "state": state_Code,
        "country": country_Code,
        "format": "json",
        "appid": api_key,

    }
    endpoint = "http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={appid}"
    url = endpoint.format(**params)
    response = requests.get(url)
    data = response.json()

    element = data
    try:
        params = {
            "lat": element[0]["lat"],
            "lon": element[0]["lon"],
            "api_key": api_key,
        }
    except:
        await ctx.send("Error: Couldn't find the location provided")
    endpoint = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    url = endpoint.format(**params)
    response = requests.get(url)
    data = response.json()
    element = data

    if element["weather"][0]["main"] == "Rain":
        description = "Bring an umbrella!"
    else:
        description = "No need to bring a umbrella :D"

    embed = discord.Embed(title=f"Wheather in {city_Name}", description=description)
    embed.add_field(name="Temperature", value=f"Cº{element['main']['temp']}")
    embed.add_field(name="Wind speed", value=f"km/h {element['wind']['speed']}")
    embed.add_field(name="Weather", value=element['weather'][0]["description"])
    await ctx.send(embed=embed)

bot.run("TOKEN")
