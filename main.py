# Allows access to Discord's API
import discord

# Gets client object from discord.py
bot = discord.Client()

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

    print("UAAP Ticket Watcher is in " + str(guild_count) + " guilds.")

bot.run("OTc0NTgzNTQxODU1ODQyMzA0.GmkR0L.fzd-QiNVVt9a2QWjZpH4yVsQDY6FQaMWwgVo38")