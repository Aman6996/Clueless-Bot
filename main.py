import os
import discord
import random
from discord import app_commands
from discord.ext import commands
# from dotenv import load_dotenv
from py_currency_converter import convert as currency_convert
from googletrans import Translator

translator = Translator()
prefix = "a!","A!", "6."
bot = commands.Bot(command_prefix=prefix,
                   intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await bot.process_commands(message)
    if f"<@{bot.user.id}>" in message.content:
        await message.reply("Type `$help` to view all available commands")

@bot.command()
async def sync(ctx, guild: discord.Guild = None):
        """Syncs the bot with the slash commands."""
        msg = await ctx.reply("Syncing app commands...")
        if guild is not None:
            bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
        await msg.edit(content="Synced app commands.")

@bot.event
async def on_reaction_add(reaction: discord.Reaction,  user: (discord.User, discord.Reaction)):
    star = "⭐"
    starboard = bot.get_channel(796492337789403156)
    if reaction.emoji in star:
        if reaction.count < 2:
            embed = discord.Embed(title=reaction.message.author,
                                  description=f"{reaction.message.content}", color=0x0dff00)
        if reaction.message.attachments:
            embed.set_image(url=reaction.message.attachments[0])
        await starboard.send(f"{reaction.message.channel.mention}", embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await ctx.message.add_reaction("❓")
    else:
        raise error


@bot.event
async def on_ready():
    print('{0.user} is now online'.format(bot))


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="\n`a!water` - Offers you water!\n\n `a!coinflip` - Flips a coin\n\n `a!getpfp` - Fetches the pfp of you **or** a given person\n\n`a!pizza` - Offers your pizza!\n\n `a!translate` - Translates text\n\n `a!whois` - Fetches the info of a user\n\n `a!guildinfo` - Displays the information of a server (also known as guild)\n\n `/convert` - Converts between currencies")
    embed.add_field(name="Not so useful commands",
                    value="`a!grabip` - grabs your ip lmao\n\n `a!deadchat` - dead chat.\n\n `a!uwu` - for... weirdos lmao\n\n `a!smile` - smiles for you\n\n")
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


@bot.command(aliases=["drink", "wotah"])
async def water(ctx):
    await ctx.reply("Here's your water!", file=discord.File("images/water.png"))


@bot.command()
async def pizza(ctx):
    await ctx.reply("Here's your Pizza!", file=discord.File("images/pizza.jpg"))


@bot.command()
async def smile(ctx):
    """smiles for you"""
    await ctx.send("<:widesmile1:826114986338025543><:widesmile2:826114986446553089><:widesmile3:826114986543153173>")


@bot.command()
async def uwu(ctx):
    embed = discord.Embed(title="owo!")
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Stylized_uwu_emoticon.svg/1200px-Stylized_uwu_emoticon.svg.png")
    await ctx.reply(embed=embed)


@bot.command(aliases=["flip"])
async def coinflip(ctx):
    await ctx.reply(random.choice(["Heads!", "Tails!"]) + " :coin:")


@bot.command(aliases=["source", "git", "code"])
async def github(ctx):
    embed = discord.Embed(
        title="CluelessBot",
        description="This bot is open source!",
        url="https://github.com/Aman6996/Clueless-Bot",
        color=ctx.author.color)
    embed.set_thumbnail(
        url="https://avatars.githubusercontent.com/u/85976860?s=400&u=170fb6e333877db6d361b3b86b82b51fb6d2a5a5&v=4")
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


@bot.command(aliases=["ched"])
async def deadchat(ctx):
    embed = discord.Embed(title="dead chat", description="You know guys, I've been thinking about something. This chat has been pretty dead seeing as nobody has talked for a while now. But I feel like that's too long of a way to describe it, so I've come up with a brand new nomenclature that's gonna blow your minds. You see if you combine the word 'chat' with the word 'dead' you get the word CHED! It's quick, concise, clear, and straight to the point. Whenever the server is inactive, don't bother trying to strike up an interesting conversation. Just say ched. It's the easiest and most efficient way to revive it! It doesn't even matter how long nobody has talked. It could be two hours or two seconds. What's the difference? It still means the server is ched. And pointing that out is extremely imperative to the server's well-being. If you don't respond to literally every instance of the server's inactivity with the repeated use of this one word, the server will plunge into darkness and despair as people never send messages ever again. So go on. Repeat the word ched with pride and honor whenever people forget to speak and revel in the sense of fulfillment and power you get from the use of the word ched.", color=ctx.author.colour)
    await ctx.send(embed=embed)


@bot.command()
async def whois(ctx, user: discord.User = None):
    if not user:
        user = ctx.message.author

    member = ctx.guild.get_member(user.id)
    avatar = user.display_avatar.with_size(4096).with_static_format("png")

    embed = discord.Embed(
        title=f"User Info - {user}",
        timestamp=ctx.message.created_at,
        color=ctx.author.color)
    embed.description = f"**Name**: {user.name}\n"
    embed.description += f"**Discriminator (tag):** {user.discriminator}\n"
    if member and member.display_name != user.name:
        embed.description += f"**Nickname**: {member.display_name}\n"
    embed.description += f"**Mention:** {user.mention}\n"
    embed.description += f"**User ID**: {user.id}\n"
    embed.description += f"**Is a bot:** {user.bot}\n"
    embed.description += f"**Account created at:** <t:{round(user.created_at.timestamp())}>\n"
    if member:
        embed.description += f"**Joined server at:** <t:{round(member.joined_at.timestamp())}>\n"
        embed.description += f"**Roles:**  {', '.join(reversed([role.mention for role in member.roles][1:]))}\n"
    embed.set_thumbnail(url=avatar)
    await ctx.reply(embed=embed)


@bot.command(aliases=["gi"])
async def guildinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(
        title="Guild info", colour=ctx.author.colour, timestamp=ctx.message.created_at)
    embed.description = f"**Name:** {guild.name}\n"
    if guild.description:
        embed.description += f"**Description:** ```\n{guild.description}```\n"
    embed.description += f"**Guild ID:** {guild.id}\n"
    embed.description += f"**Created at:** <t:{round(guild.created_at.timestamp())}>\n"
    embed.description += f"**Owner:** {guild.owner.mention}\n"
    embed.description += f"**Verification level:** {guild.verification_level}\n"
    embed.description += f"**Filesize limit:** {round(guild.filesize_limit/(1000000))}MB\n"
    embed.description += f"**Boost level:** {guild.premium_tier} ({guild.premium_subscription_count} Boosts)\n"
    if guild.premium_subscriber_role:
        embed.description += f"**Server booster role:** {guild.premium_subscriber_role.mention}\n\n"
    human = [member for member in guild.members if not member.bot]
    bot = [member for member in guild.members if member.bot]
    embed.description += f"**Members:** {guild.member_count}/{guild.max_members} (🤖{len(bot)} | 👤{len(human)})\n"
    embed.description += f"**Emojis:** {len(guild.emojis)}/{guild.emoji_limit}\n"
    embed.description += f"**Roles:** {len(guild.roles)}\n"
    embed.description += f"**Stickers:** {len(guild.stickers)}/{guild.sticker_limit}\n"
    embed.description += f"**Channels:** {len(guild.channels)} (⌨️{len(guild.text_channels)} 🔈{len(guild.voice_channels)} 🎭{len(guild.stage_channels)})\n"
    embed.set_image(url=guild.banner)
    embed.set_thumbnail(url=guild.icon)
    await ctx.reply(embed=embed)


@bot.command(aliases=["ts"])
async def translate(ctx, *, user_input, user: discord.User = None):
    tr = translator.translate(f"{user_input}")
    text = tr.text
    TransDict = {"af": "Afrikaans", "sq": "Albanian", "am": "Amharic", "ar": "Arabic", "hy": "Armenian", "az": "Azerbaijani", "eu": "Basque", "be": "Belarusian", "bn": "Bengali", "bs": "Bosnian", "bg": "Bulgarian", "ca": "Catalan", "ceb": "Cebuano", "zh-CN": "Chinese (Simplified)", "zh-TW": "Chinese (Traditional)", "co": "Corsican", "hr": "Croatian", "cs": "Czech", "da": "Danish", "nl": "Dutch", "en": "English", "eo": "Esperanto", "et": "Estonian", "fi": "Finnish", "fr": "French", "fy": "Frisian", "gl": "Galician", "ka": "Georgian", "de": "German", "el": "Greek", "gu": "Gujarati", "ht": "Haitian Creole", "ha": "Hausa", "haw": "Hawaiian", "iw": "Hebrew", "hi": "Hindi", "hmn": "Hmong", "hu": "Hungarian", "is": "Icelandic", "ig": "Igbo", "id": "Indonesian", "ga": "Irish", "it": "Italian", "ja": "Japanese", "jw": "Javanese", "kn": "Kannada", "kk": "Kazakh", "km": "Khmer", "ko": "Korean", "ku": "Kurdish", "ky": "Kyrgyz", "lo": "Lao", "la": "Latin",
                 "lv": "Latvian", "lt": "Lithuanian", "lb": "Luxembourgish", "mk": "Macedonian", "mg": "Malagasy", "ms": "Malay", "ml": "Malayalam", "mt": "Maltese", "mi": "Maori", "mr": "Marathi", "mn": "Mongolian", "my": "Myanmar (Burmese)", "ne": "Nepali", "no": "Norwegian", "ny": "Nyanja (Chichewa)", "ps": "Pashto", "fa": "Persian", "pl": "Polish", "pt": "Portuguese (Portugal, Brazil)", "pa": "Punjabi", "ro": "Romanian", "ru": "Russian", "sm": "Samoan", "gd": "Scots Gaelic", "sr": "Serbian", "st": "Sesotho", "sn": "Shona", "sd": "Sindhi", "si": "Sinhala (Sinhalese)", "sk": "Slovak", "sl": "Slovenian", "so": "Somali", "es": "Spanish", "su": "Sundanese", "sw": "Swahili", "sv": "Swedish", "tl": "Tagalog (Filipino)", "tg": "Tajik", "ta": "Tamil", "te": "Telugu", "th": "Thai", "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu", "uz": "Uzbek", "vi": "Vietnamese", "cy": "Welsh", "xh": "Xhosa", "yi": "Yiddish", "yo": "Yoruba", "zu": "Zulu"}
    TranslatedFrom = discord.Embed(
        title="Translated from " + TransDict[tr.src], description=f"{user_input}", color=ctx.author.colour)
    TranslatedTo = discord.Embed(
        title="Translated to English", description=tr.text, color=ctx.author.colour)
    await ctx.reply(embeds=[TranslatedFrom, TranslatedTo])


@bot.command(aliases=["ip", "genip"])
async def grabip(ctx):
    ip = []
    for i in range(4):
        ip.append(str(random.randint(0, 255)))
    await ctx.reply(".".join(ip))

@bot.tree.command()
async def sayhello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@bot.tree.command()
@app_commands.describe(
    amount= 'How much to convert',
    base= 'The initial currency to convert from',
    to= 'The currency to convert to'
)
async def convert(interaction: discord.Interaction, amount: int, base: str, to: str):
    currency_convert(base=base, amount=amount, to=[to])
    new_amount = currency_convert(base=base, amount=amount, to=[to])[to]
    embed = discord.Embed(title="Converted", description=f"**Amount:** {amount} -> {new_amount}\n **Currency:** {base} -> {to}")
    await interaction.response.send_message(embed=embed)



# load_dotenv()
# bot.run(os.getenv("TOKEN"))
bot.run("ODQ3NDU5ODQxNDEyOTU2MTYw.Gc0Z5e.EJ1uyv7Chi6dFptvRPp1Foj6IecJEHQCNGsV_Q")
