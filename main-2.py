import os
import discord
from discord.ext import commands, tasks
from googletrans import Translator
import random

intents = discord.Intents.all()
intents.members = True

# Set up the Discord client
bot = commands.Bot(command_prefix='/', intents=intents)

status_messages = [
    "Checking non-English words",
    "Translating sentences",
    "Learning new languages",
    "Helping users communicate",
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    change_status.start()

@tasks.loop(minutes=1)
async def change_status():
    new_status = random.choice(status_messages)
    await bot.change_presence(activity=discord.Game(name=new_status))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    translator = Translator()
    translation = translator.translate(message.content, dest='en')
    await message.channel.send(translation.text)

# Get the bot token from an environment variable
token = os.environ.get('DISCORD_BOT_TOKEN')
bot.run('MTE1NjIyODIyOTc1Mzk5OTM5Mg.GfgZow.L4eBl72END5nEr1dLanZk5iVsnZg0QFVCKR3wc')

