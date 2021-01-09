import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = '.', case_insensitive=True)

dew_list = ["Well said fellow Dew Mate, and make sure to grab and ice cold Mountain Dew before gaslighting your friends!", "Dew what you think is best, but make sure you have an ice cold Mountain Dew in your hands!", "Dew you guys ever think about what your purpose is in life? Like, are we all just corporate shill's designed to please PepsiCo or is that just me?", "As Chancellor Palpatine once said: Dew it!"]

trigger_phrases = ['do the dew']

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    for word in trigger_phrases:
      if message.author == client.user:
        return
      if word in message.content.lower():
        response = random.choice(dew_list)
        await message.channel.send(response)
   

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
