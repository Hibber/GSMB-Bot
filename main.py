import datetime
import nextcord
import os
import requests

from blizzardapi import BlizzardApi
from dotenv import load_dotenv
from nextcord.ext import commands


from auth import get_token

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
bot = commands.Bot(command_prefix="!")
access_token = os.getenv("ACCESS_TOKEN")
api = BlizzardApi(os.getenv("WOW_CLIENT_ID"), os.getenv("WOW_CLIENT_SECRET"))


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    await bot.change_presence(
        status=nextcord.Status.online, activity=nextcord.Game("!help")
    )
    print(access_token)


@bot.command(name="token", help="Get WoW token price")
async def get_wow_token(ctx):
    """get the current wow token price"""
    url = (
        "https://us.api.blizzard.com/data/wow/token/?namespace=dynamic-us&locale=en_US"
    )
    headers = {"Authorization": "Bearer {}".format(access_token)}
    response = requests.get(url, headers=headers).json()
    token = response["price"]
    formatted = int(str(int(str(token)[::-1]))[::-1])
    text_title = "🪙Current Token Price for US🪙"
    embed = nextcord.Embed(title=text_title + "\n\n", color=0x00FF00,
                           description='**Price:** ' + f"**`{formatted}`**")
    await ctx.send("<@" + str(ctx.author.id) + ">")
    embed.set_author(
        name="GSMB Bot", url="https://worldofwarcraft.com/en-us/token",
        icon_url="https://render.worldofwarcraft.com/us/guild/crest/69/emblem-69-b1b8b1"
                 "-232323.jpg",
    )
    embed.set_thumbnail(
        url="https://render.worldofwarcraft.com/us/guild/crest/69/emblem-69-b1b8b1"
            "-232323.jpg"
    )
    embed.set_footer(
        text="🌐 " + datetime.datetime.now().strftime("%A " + "at: " + "%H:%M" + "%p")
    )
    channel = await bot.fetch_channel(960708949127102484)
    await channel.send(embed=embed)


# @bot.command(name="character")
# async def get_profile(ctx):
#     """get the profile of a player"""
#     name = input("Enter the name of the character: ")
#     url = (
#         "https://us.api.blizzard.com/profile/wow/character/"
#         + name
#         + "/?namespace=dynamic-us&locale=en_US"
#     )
#     headers = {"Authorization": "Bearer USGgbCdyLp4m8oAe7SanuzRttArodo7cGc"}
#     response = requests.get(url, headers=headers, auth=access_token)
#     print(response)
#     await ctx.send(response)
#     # api.wow.get_profile()

def main():
    bot.run(bot_token)
    # get_token()


if __name__ == "__main__":
    main()
