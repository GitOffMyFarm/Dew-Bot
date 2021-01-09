import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands
#imports libraries needed to run Dew Bot

client = discord.Client()
#Creates the python object Discord Client used to send the commands to Discord's server.

dew_list = ["Well said fellow Dew Mate, and make sure to grab and ice cold Mountain Dew before gaslighting your friends!", "Dew what you think is best, but make sure you have an ice cold Mountain Dew in your hands!", "Dew you guys ever think about what your purpose is in life? Like, are we all just corporate shill's designed to please PepsiCo or is that just me?", "As Chancellor Palpatine once said: Dew it!"]
#Creates a list of phrases for Dew Bot to pull from later.

trigger_phrases = ['do the dew']
#List of phrases for Dew Bot to respond to, hoping to add function to allow user's in Discord Server to add to phrases which is why it's a list not a string.

@client.event
#creates a client event which triggers the bot to modify based on the function below. 
async def on_ready():
  #Runs events asynchronously rather than top to bottom.
    print("I'm in")
    print(client.user)
    #Prints phrase in console letting us know bot has connected to server.

@client.event
async def on_message(message):
    for word in trigger_phrases:
      #Creates an event if someone says a phrase from the "trigger_phrases" list.
      if message.author == client.user:
        return
        #If the message content comes from Dew Bot it won't respond with a message eliminating forever loops.
      if word in message.content.lower():
        #If someone has a phrase from "trigger_phrases" in their message that's not case sensitive.
        response = random.choice(dew_list)
        #Respond with a random string from "Dew_list"
        await message.channel.send(response)
        #Send the response in a message back to channel.

keep_alive()
#Accesses web server created in keep_alive.py to keep bot running after repl is closed.
token = os.environ.get("BOT_TOKEN")
client.run(token)
#Accesses bot token from .env to connect to Discord bot.
