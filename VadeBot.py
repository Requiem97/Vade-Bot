import os
import random
import discord
import glob
import datetime
import asyncio
import logging
from discord.ext.commands import Bot
from util import db

bot = Bot(description="FUCK THIS SHIT", command_prefix=os.environ["Command_Prefix"], pm_help=False)
extensions = ['Utility', 'Mathematics', 'Vade', 'NOHK']
# extensions = ['Utility', 'Mathematics', 'Vade', 'NOHK', 'Rainbow6']

file_list = glob.glob(os.path.join(os.getcwd(), "files/prompts", "*.txt"))
#file_list = glob.glob(os.path.join(os.getcwd(), "files/prompts", "endgame.txt"))
wait = None

messages = []
for path in file_list:
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            messages.append(line)

card_list = []
for file in os.listdir("cards"):
    if file.lower().endswith(".png") or file.lower().endswith(".jpg"):
        card_list.append('cards/{}'.format(file))
card_map = [x.replace("cards/", "").replace(".png",
                                               "").replace(".jpg", "").lower() for x in card_list]

def bobo_tag(user_id):
    return 'BOBO MO <@{!s}>'.format(user_id)

def find_Bobo(words):
    return 'bobo' in words

@bot.event
async def on_ready():
    db.connect()
    guild = await bot.fetch_guilds().flatten()
    print('Logged in as ' + bot.user.name + ' (ID:' + str(bot.user.id) + ') | Connected to ' + str(
        len(guild)) + ' servers | Connected to ' + str(
        len(set(bot.get_all_members()))) + ' users')
    # type 1 = playing, 2 = listeningto, 3 = watching
    await bot.change_presence(activity=discord.Game('ANAL CHILD PORN WHILE FUCKING CHILDREN'))

@bot.event
async def on_message(message):
    user_id = message.author.id
    print(message)
    words = message.content.lower().split()
    if user_id != bot.user.id and message.guild.id != 607181202922799135:
        if message.content.lower() == "good vade":
            await message.channel.send(file=discord.File('pics/vadesmile.jpg'))
        elif message.content.lower() == "bad vade":
            await message.channel.send(file=discord.File('pics/badvade.jpg'))
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