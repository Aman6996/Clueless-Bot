import os
import discord

from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands
prefix = "$", "6."
bot = commands.Bot(command_prefix=prefix, intents= discord.Intents.all())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await bot.process_commands(message)
        if bot.user in message.mentions:
                await message.channel.send("HEY")
                       
@bot.event
async def on_ready():
    print('{0.user} is now online'.format(bot))

@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")

# @bot.command()
# async def image(ctx):
#     await ctx.reply(file=discord.File("images/2022-07-07_14-54.png"))

@bot.command()
async def water(ctx):
    await ctx.reply(file=discord.File("images/drink.png"))

@bot.command()
async def smile(ctx):
    await ctx.send("<:widesmile1:826114986338025543><:widesmile2:826114986446553089><:widesmile3:826114986543153173>")

@bot.command()
async def uwu(ctx):
    embed = discord.Embed(title="owo!") 
    embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Stylized_uwu_emoticon.svg/1200px-Stylized_uwu_emoticon.svg.png")
    await ctx.reply(embed=embed)

@bot.command()
async def user_input(ctx, *, user_input):
    print(user_input)
    with open('input.txt', 'a') as f:
        f.write(user_input + "\n")

bot.run(os.getenv("TOKEN"))