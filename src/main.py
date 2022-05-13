import discord
import os

from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

import website_checker

bot = discord.Client()

bot.run(DISCORD_TOKEN)