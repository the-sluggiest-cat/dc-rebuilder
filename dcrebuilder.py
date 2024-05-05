import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="dc!", intents=intents)

#we're doing the thing! wwe hav erobot
@bot.event
async def on_ready():
    print("Signed in as %s!" %bot.user)

bot.run(open("token.txt", "r").read())
