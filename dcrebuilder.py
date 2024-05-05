import discord, print_colors
from print_colors import dprint, iprint, wprint, eprint, tprint
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="dc!", intents=intents, help_command=None)

# S: we're doing the thing! wwe hav erobot 
@bot.event
async def on_ready():
    iprint("Signed in as %s!" %bot.user, "on_ready")
    iprint("We are currently in %s guild(s)" %len(bot.guilds), "on_ready")

@bot.command(name="sync")
async def __sync(ctx: commands.Context):
    if ctx.author.name not in ["slugcat.exe", "rawboot"]: return # S: if not one of us, fuck you!
    iprint("Syncing commands to Discord...", "__sync")
    await bot.tree.sync()
    await ctx.message.add_reaction("✅")
    iprint("Done syncing.", "__sync")

@bot.event
async def on_guild_join(guild: discord.Guild): 
    iprint("Got a new guild named %s! We are now in %s guild(s)." %(guild.name, len(bot.guilds)), "on_guild_join") # S: yay! new guild!

@bot.event
async def on_guild_remove(guild: discord.Guild):
    iprint("We just lost a guild! %s removed us. Now I'm sad. We are now in %s guild(s)." %(guild.name, len(bot.guilds)), "on_guild_remove") # S: im gonna beat you to death.

bot.run(open("token.txt", "r").read())
