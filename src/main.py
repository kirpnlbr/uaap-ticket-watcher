import discord
import os

from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

bot.run(DISCORD_TOKEN)