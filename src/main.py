import discord
import os

from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

from website_checker import change_value

bot = discord.Client()

@bot.event
async def on_message(message):
    if change_value is True:
        await message.channel.send('Looks like an event has been added or removed from SM Tickets. Go check it out quick 👀 https://smtickets.com/events/category/sports')

bot.run(DISCORD_TOKEN)