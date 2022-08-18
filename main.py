# BEFORE SENDING TO REPLIT DO THESE CHANGES
#Top of Main.py

# from webserver import keep_alive

#Bottom of Main.py

# keep_alive()

# TOKEN = os.environ.get("DISCORD_BOT_SECRET")

# bot.run(TOKEN)


import os
import discord
import random

from dotenv import load_dotenv
load_dotenv()



from discord.ext import commands
prefix = "$", "6."
bot = commands.Bot(command_prefix=prefix, intents= discord.Intents.all(), case_insensitive=True)





@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await bot.process_commands(message)
        if bot.user in message.mentions:
                await message.channel.send("Type `$help` to view all available commands")


@bot.event
async def on_ready():
    print('{0.user} is now online'.format(bot))


@bot.command(aliases=["hello"])
async def hi(ctx):
    await ctx.reply("Hello!")


# @bot.command()
# async def image(ctx):
#     await ctx.send(file=discord.File("images/2022-07-07_14-54.png"))


@bot.command(aliases=["water"])
async def drink(ctx):
    await ctx.reply(file=discord.File("images/water.png"))


@bot.command()
async def smile(ctx):
    await ctx.send("<:widesmile1:826114986338025543><:widesmile2:826114986446553089><:widesmile3:826114986543153173>")


# @bot.command()
# async def user_input(ctx, *, user_input):
#     print(user_input)
#     with open('input.txt', 'a') as f:
#         f.write(user_input + "\n")


@bot.command()
async def uwu(ctx):
    embed = discord.Embed(title="owo!") 
    embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Stylized_uwu_emoticon.svg/1200px-Stylized_uwu_emoticon.svg.png")
    await ctx.reply(embed=embed)


@bot.command()
async def sayyourtoken(ctx):
    await ctx.send("stfu")


@bot.command(aliases=["flip"])
async def coinflip(ctx):
        await ctx.reply(random.choice(["Heads!", "Tails!"]) + " :coin:")





bot.run(os.getenv("TOKEN"))