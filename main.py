"""BEFORE SENDING TO REPLIT DO THESE CHANGES
Top of Main.py

from webserver import keep_alive

Bottom of Main.py

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)"""


from email import message
import os
import discord
import random

from dotenv import load_dotenv
load_dotenv()



from discord.ext import commands
prefix = "$", "6."
bot = commands.Bot(command_prefix=prefix, intents= discord.Intents.all(), case_insensitive=True)
bot.remove_command("help")




@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await bot.process_commands(message)
        if f"<@{bot.user.id}>" in message.content:
                await message.reply("Type `$help` to view all available commands")
        #   to annoy a person called Velvet lmfao
        for q in ['almond', 'sparking', 'tea knight', 'lilac', 'herb', 'clotted cream', 'licorice', 'espresso', 'madeleine']:
          if q in message.content.lower() and not f'"{q}"' in message.content.lower():
            await message.reply('https://www.pearson.com/uk/learners/primary-parents/learn-at-home/help-your-child-to-enjoy-reading/why-is-reading-so-important.html')



# @bot.event
# async def on_command_error(ctx, error):
#     # If the command does not exist/is not found.
#     if isinstance(error, commands.CommandNotFound):
#         return await ctx.message.add_reaction("❓")
#     else:
#         raise error

@bot.event
async def on_ready():
    print('{0.user} is now online'.format(bot))


@bot.command()
async def ping(ctx):
    ping = round(bot.latency * 1000, 2)

    if ping < 100:
        color = 0x0dff00
    elif ping > 100 and ping < 150:
        color = 0xff4800
    else:
        color = 0xff0000

    await ctx.send(embed=discord.Embed(
        title="Ping", description=f"{ping} ms", color=color))


"""Hard coded help command lmfao"""
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="\n`$water` - Offers you water!\n\n `$coinflip` - Flips a coin\n\n `$getpfp` - Fetches the pfp of you **or** a given person\n\n `$smile` Smiles for you!\n\n `$uwu` - For... weirdos lmao",color=ctx.author.color)
    embed.add_field(name="Unlisted Commands", value="`$hi`, `$hello` - Casual greeting lmao\n\n `$sayyourtoken` - idk try it yourself")
    await ctx.reply(embed=embed)


@bot.command(aliases=["hello"])
async def hi(ctx):
    await ctx.reply("Hello!")


# @bot.command()
# async def image(ctx):
#     await ctx.send(file=discord.File("images/2022-07-07_14-54.png"))


@bot.command(aliases=["drink", "wotah"])
async def water(ctx):
    """offers wotah"""
    await ctx.reply(file=discord.File("images/water.png"))


@bot.command()
async def smile(ctx):
    """smiles for you"""
    await ctx.send("<:widesmile1:826114986338025543><:widesmile2:826114986446553089><:widesmile3:826114986543153173>")


# @bot.command()
# async def user_input(ctx, *, user_input):
#     print(user_input)
#     with open('input.txt', 'a') as f:
#         f.write(user_input + "\n")


@bot.command()
async def uwu(ctx):
    embed = discord.Embed(title="owo!") 
    """for weirdos"""
    embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Stylized_uwu_emoticon.svg/1200px-Stylized_uwu_emoticon.svg.png")
    await ctx.reply(embed=embed)


@bot.command()
async def sayyourtoken(ctx):
    """idk"""
    await ctx.send("no")


@bot.command(aliases=["flip"])
async def coinflip(ctx):
        """flips a coin"""
        await ctx.reply(random.choice(["Heads!", "Tails!"]) + " :coin:")


@bot.command(aliases=["source", "git", "code"])
async def github(ctx):
    embed = discord.Embed(
            title="CluelessBot",
            description="This bot is open source!",
            url="https://github.com/Aman6996/Clueless-Bot",
            color=ctx.author.color)
    """links to github"""        
    await ctx.reply(embed=embed)

@bot.command(aliases=["pfpget", "gpfp", "pfp"])

async def getpfp(ctx: commands.Context, user: discord.User = None):
        if not user:
            user = ctx.message.author
        avatar = user.display_avatar.with_size(4096).with_static_format("png")

        embed = discord.Embed(
            colour=user.colour,
            timestamp=ctx.message.created_at,
            title=f"{user.display_name}'s pfp",
        )
        embed.set_image(url=avatar)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)



# @bot.command()
# @commands.is_owner()
# async def test(ctx):
#     await ctx.message.add_reaction("🔐")


@bot.command()
@commands.is_owner()
async def user_input(ctx, *, user_input):
    exec(user_input)
    await ctx.reply(exec(user_input))






bot.run(os.getenv("TOKEN"))
