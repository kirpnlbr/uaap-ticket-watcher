import discord
import os

from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

from website_checker import change_value
from website_checker import error

bot = discord.Client()

@bot.event
async def on_message(message):
    if change_value is True:
        await message.channel.send('Looks like an event has been added or removed from SM Tickets. Go check it out quick 👀 https://smtickets.com/events/category/sports')

    elif error is True:
        await message.channel.send('An error has occurred woops. Fix me pls')

bot.run(DISCORD_TOKEN)