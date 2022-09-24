"""BEFORE SENDING TO REPLIT DO THESE CHANGES
Top of Main.py

from webserver import keep_alive

Bottom of Main.py

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)"""





import asyncio
import os
import discord
import random
from googletrans import Translator
translator = Translator()
import requests
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
        #   to annoy a person called Velvet lmfao
    for q in ['almond', 'sparking', 'tea knight', 'lilac', 'herb', 'clotted cream', 'madeleine', 'caramel arrow', 'wolf', 'milk', 'raspberry', 'vampire']:
        if message.author.id == 1004534564246523965:
          if q in message.content.lower() and not f'"{q}"' in message.content.lower():
            await message.reply('https://www.pearson.com/uk/learners/primary-parents/learn-at-home/help-your-child-to-enjoy-reading/why-is-reading-so-important.html')
            break
        else:
          return
    if f"<@{bot.user.id}>" in message.content:
            await message.reply("Type `$help` to view all available commands")
   # if 'belbet' in message.content:
   #     await message.reply('yes, belbet')



    # beep boop testing testing
    # if message.content == "deeeez":
    #     await message.channel.send("your nuts are cool " + f"{message.author}" + "!")


@bot.event
async def on_command_error(ctx, error):
    # If the command does not exist/is not found.
    if isinstance(error, commands.CommandNotFound):
        return await ctx.message.add_reaction("❓")
    else:
        raise error

@bot.event
async def on_ready():
    print('{0.user} is now online'.format(bot))

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="\n`$water` - Offers you water!\n\n `$coinflip` - Flips a coin\n\n `$getpfp` - Fetches the pfp of you **or** a given person\n\n `$smile` Smiles for you!\n\n `$uwu` - For... weirdos lmao\n\n `$pizza` - Offers your pizza!\n\n `$translate` - Translates text")
    embed.add_field(name="Unlisted Commands", value="`$hi`, `$hello` - Casual greeting lmao\n\n `$sayyourtoken` - idk try it yourself\n\n `$grabip` - grabs your ip lmao\n\n `$deadchat` - dead chat.")
    await ctx.reply(embed=embed)


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



@bot.command(aliases=["hello"])
async def hi(ctx):
    await ctx.reply("Hello!")


# @bot.command()
# async def image(ctx):
#     await ctx.send(file=discord.File("images/2022-07-07_14-54.png"))


@bot.command(aliases=["drink", "wotah"])
async def water(ctx):
    """offers wotah"""
    await ctx.reply("Here's your water!", file=discord.File("images/water.png"))

@bot.command()
async def pizza(ctx):
  await ctx.reply("Here's your Pizza!", file=discord.File("images/pizza.jpg"))


@bot.command()
async def smile(ctx):
    """smiles for you"""
    await ctx.send("<:widesmile1:826114986338025543><:widesmile2:826114986446553089><:widesmile3:826114986543153173>")


@bot.command()
async def yes(ctx, *, user_input):
    print(user_input)
    await ctx.reply(user_input)
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


@bot.command(aliases=["ched"])
async def deadchat(ctx):
  embed = discord.Embed(title="dead chat", description="You know guys, I've been thinking about something. This chat has been pretty dead seeing as nobody has talked for a while now. But I feel like that's too long of a way to describe it, so I've come up with a brand new nomenclature that's gonna blow your minds. You see if you combine the word 'chat' with the word 'dead' you get the word CHED! It's quick, concise, clear, and straight to the point. Whenever the server is inactive, don't bother trying to strike up an interesting conversation. Just say ched. It's the easiest and most efficient way to revive it! It doesn't even matter how long nobody has talked. It could be two hours or two seconds. What's the difference? It still means the server is ched. And pointing that out is extremely imperative to the server's well-being. If you don't respond to literally every instance of the server's inactivity with the repeated use of this one word, the server will plunge into darkness and despair as people never send messages ever again. So go on. Repeat the word ched with pride and honor whenever people forget to speak and revel in the sense of fulfillment and power you get from the use of the word ched.", color=ctx.author.colour)
  await ctx.send(embed=embed)


# WIP
@bot.command()
async def whois(ctx, user: discord.User = None):
    if not user:
            user = ctx.message.author
    member = ctx.guild.get_member(user.id)
    """Used for getting nickname"""
    avatar = user.display_avatar.with_size(4096).with_static_format("png")
    """Used for setting thumbnail"""
    embed = discord.Embed(
            title=f"User Info - {user}",
            timestamp=ctx.message.created_at)
    embed.description = f"**Name**: {user.name}\n"
    embed.description += f"**Discriminator (tag):** {user.discriminator}\n"
    embed.description += f"**Nickname**: {member.display_name}\n"
    embed.description += f"**User ID**: {user.id}\n"
    embed.description += f"**Mention:** {user.mention}\n"
    embed.description += f"**Is a bot:** {user.bot}\n"
    embed.description += f"**Account created at:** <t:{round(user.created_at.timestamp())}>\n"
    embed.description += f"**Joined server at:** <t:{round(member.joined_at.timestamp())}>"
    embed.set_thumbnail(url=avatar)
    await ctx.reply(embed=embed)




@bot.command(aliases=["ts"])
async def translate(ctx, *, user_input, user: discord.User = None):
    tr = translator.translate(f"{user_input}")
    text = tr.text
    TransDict={"af": "Afrikaans", "sq": "Albanian", "am": "Amharic", "ar": "Arabic", "hy": "Armenian", "az": "Azerbaijani", "eu": "Basque", "be": "Belarusian", "bn": "Bengali", "bs": "Bosnian", "bg": "Bulgarian", "ca": "Catalan", "ceb": "Cebuano", "zh-CN": "Chinese (Simplified)", "zh-TW": "Chinese (Traditional)", "co": "Corsican", "hr": "Croatian", "cs": "Czech", "da": "Danish", "nl": "Dutch", "en": "English", "eo": "Esperanto", "et": "Estonian", "fi": "Finnish", "fr": "French", "fy": "Frisian", "gl": "Galician", "ka": "Georgian", "de": "German", "el": "Greek", "gu": "Gujarati", "ht": "Haitian Creole", "ha": "Hausa", "haw": "Hawaiian", "iw": "Hebrew", "hi": "Hindi", "hmn": "Hmong", "hu": "Hungarian", "is": "Icelandic", "ig": "Igbo", "id": "Indonesian", "ga": "Irish", "it": "Italian", "ja": "Japanese", "jw": "Javanese", "kn": "Kannada", "kk": "Kazakh", "km": "Khmer", "ko": "Korean", "ku": "Kurdish", "ky": "Kyrgyz", "lo": "Lao", "la": "Latin", "lv": "Latvian", "lt": "Lithuanian", "lb": "Luxembourgish", "mk": "Macedonian", "mg": "Malagasy", "ms": "Malay", "ml": "Malayalam", "mt": "Maltese", "mi": "Maori", "mr": "Marathi", "mn": "Mongolian", "my": "Myanmar (Burmese)", "ne": "Nepali", "no": "Norwegian", "ny": "Nyanja (Chichewa)", "ps": "Pashto", "fa": "Persian", "pl": "Polish", "pt": "Portuguese (Portugal, Brazil)", "pa": "Punjabi", "ro": "Romanian", "ru": "Russian", "sm": "Samoan", "gd": "Scots Gaelic", "sr": "Serbian", "st": "Sesotho", "sn": "Shona", "sd": "Sindhi", "si": "Sinhala (Sinhalese)", "sk": "Slovak", "sl": "Slovenian", "so": "Somali", "es": "Spanish", "su": "Sundanese", "sw": "Swahili", "sv": "Swedish", "tl": "Tagalog (Filipino)", "tg": "Tajik", "ta": "Tamil", "te": "Telugu", "th": "Thai", "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu", "uz": "Uzbek", "vi": "Vietnamese", "cy": "Welsh", "xh": "Xhosa", "yi": "Yiddish", "yo": "Yoruba", "zu": "Zulu"}
    TranslatedFrom = discord.Embed(title="Translated from "+ TransDict[tr.src], description=f"{user_input}")
    TranslatedTo = discord.Embed(title="Translated to English", description=tr.text)
    await ctx.reply(embeds=[TranslatedFrom, TranslatedTo])

# @bot.command()
# async def test(ctx):
#     await asyncio.sleep(123)
#     await ctx.send("heeey
# ")

@bot.command(aliases=["ip", "genip"])
async def grabip(ctx):
    ip = []
    for i in range(4):
        ip.append(str(random.randint(0, 255)))
    await ctx.reply(".".join(ip))

# @bot.command()
# async def test(ctx, user: discord.User = None):
#     if not user:
#             user = ctx.message.author
#     await ctx.reply()


bot.run(os.getenv("TOKEN"))
