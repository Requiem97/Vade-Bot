import os
import random
import discord
import glob
import datetime
import asyncio
import logging
from discord.ext.commands import Bot
from src.util import db

bot = Bot(description="FUCK THIS SHIT", command_prefix=os.environ["Command_Prefix"], pm_help=False)
extensions = ['Mathematics']
# extensions = ['Utility', 'Mathematics', 'Vade', 'NOHK', 'Rainbow6']

file_list = glob.glob(os.path.join(os.getcwd(), "src/files/prompts", "*.txt"))
#file_list = glob.glob(os.path.join(os.getcwd(), "src/files/prompts", "endgame.txt"))
wait = None

messages = []
for path in file_list:
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            messages.append(line)

pic_list = []
for file in os.listdir("src/pics"):
    if file.lower().endswith(".png") or file.lower().endswith(".jpg"):
        pic_list.append('src/pics/{}'.format(file))

card_list = []
for file in os.listdir("src/cards"):
    if file.lower().endswith(".png") or file.lower().endswith(".jpg"):
        card_list.append('src/cards/{}'.format(file))
card_map = [x.replace("src/cards/", "").replace(".png",
                                               "").replace(".jpg", "").lower() for x in card_list]

ball_replies = []
with open("src/files/8ballReplies.txt") as file:
    ball_replies = [line.strip() for line in file]

#mudae_ids = ["432610292342587392", "588992629136424960", "531931447129538588"]

def bobo_tag(user_id):
    return 'BOBO MO <@{!s}>'.format(user_id)


def find_Bobo(words):
    return 'bobo' in words

@bot.event
async def on_ready():
    db.connect()
    guild = await bot.fetch_guilds().flatten()
    print(guild)
    print('Logged in as ' + bot.user.name + ' (ID:' + str(bot.user.id) + ') | Connected to ' + str(
        len([1,2])) + ' servers | Connected to ' + str(
        len(set(bot.get_all_members()))) + ' users')
    # type 1 = playing, 2 = listeningto, 3 = watching
    await bot.change_presence(activity=discord.Game('ANAL CHILD PORN WHILE FUCKING CHILDREN'))

@bot.event
async def on_message(message):
    user_id = message.author.id
    print(message)
    words = message.content.lower().split()
    #if (user_id in mudae_ids and message.embeds):
    #    await bot.add_reaction(message, u"\u2B05")
    #    await bot.add_reaction(message, u"\u27A1")
    #    await asyncio.sleep(3)
    #    await bot.add_reaction(message, 	u"\U0001F496")
    if user_id != bot.user.id and message.guild.id != 607181202922799135:
        if message.content.startswith('v!8ball'):
            if len(words) == 1:
                await message.channel.send("THAT AIN'T A FUCKING QUESTION FFS")
            else:
                await message.channel.send(random.choice(ball_replies))
        elif message.content.lower() == "good vade":
            await message.channel.send(file=discord.File('src/pics/vadesmile.jpg'))
        elif message.content.lower() == "bad vade":
            await message.channel.send(file=discord.File('src/pics/badvade.jpg'))
        elif find_Bobo(words):
            await message.channel.send(bobo_tag(user_id))
        elif random.randint(1, 100) <= 3:
            msg = random.choice(messages)
            await message.channel.send(msg)
    await bot.process_commands(message)

if __name__ == '__main__':
    print('Checking for Command cogs')
    logging.info('Checking for Command cogs')
    for extension in extensions:
        try:
            print('Loading %s cog', extension)
            logging.info('Loading %s cog', extension)
            bot.load_extension('commands.{}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(
                'commands.{}'.format(extension), exc))
    print('Running bot')
    logging.info('Running Bot')
    bot.run(os.environ['VadeBot_Token'])
