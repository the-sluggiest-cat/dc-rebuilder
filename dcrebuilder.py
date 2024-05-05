import discord, print_colors, dataset
from print_colors import dprint, iprint, wprint, eprint, tprint
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="dc!", intents=intents, help_command=None)

db = dataset.connect("sqlite:///data/dcrebuilder.db")

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

@bot.command(name="sauron")
async def __eye_of_sauron_reveal_your_truth(ctx: commands.Context):
    if ctx.author.name not in ["slugcat.exe", "rawboot"]: return # S: if not one of us, fuck you!
    categories = ctx.guild.by_category()
    table = db[str(ctx.guild.id)]
    thingy = table.find_one(name="__fuckyouinator__lmao__idiot")
    if thingy is not None:
        iprint("WHAT", "__eosryt")
        iprint(thingy, "__eosryt")
        return
    for category in categories:
        row = {"name": category[0].name if category[0] is not None else "__fuckyouinator__lmao__idiot"}
        for index, channel in enumerate(category[1]):
            row[channel.name] = index
        table.insert(row)
    db.commit()
    iprint(":3", "__eosryt")
    for thingy in table:
        iprint(thingy, "__eosryt")

@bot.event
async def on_guild_join(guild: discord.Guild): 
    iprint("Got a new guild named %s! We are now in %s guild(s)." %(guild.name, len(bot.guilds)), "on_guild_join") # S: yay! new guild!
    iprint("Creating a duplicate of this guild right now.", "on_guild_join")
    thingy = guild.by_category()
    for thing in thingy:
        iprint(thing, "on_guild_join")
    

@bot.event
async def on_guild_remove(guild: discord.Guild):
    iprint("We just lost a guild! %s removed us. Now I'm sad. We are now in %s guild(s)." %(guild.name, len(bot.guilds)), "on_guild_remove") # S: im gonna beat you to death.

bot.run(open("token.txt", "r").read())
