import discord
import os

from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

from scripts.website_checker import change_value
from scripts.website_checker import script_error

bot = discord.Client()

@bot.event
async def on_message(message):
    if change_value is True:
        await message.channel.send('Looks like an event has been added or removed from SM Tickets. Tignan mo na dali!! https://smtickets.com/events/category/sports')

    elif script_error is True:
        await message.channel.send('404. Fix me pls')

bot.run(DISCORD_TOKEN)