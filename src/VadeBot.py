import os
import random
import discord
import glob
import datetime
import asyncio
from discord.ext.commands import Bot
from src.util import db

client = Bot(description="FUCK THIS SHIT", command_prefix="v!", pm_help=False)
extensions = ['Utility', 'Mathematics', 'Vade', 'NOHK', 'Rainbow6']

user_id = '0'
file_list = glob.glob(os.path.join(os.getcwd(), "src/files/prompts", "*.txt"))
#file_list = glob.glob(os.path.join(os.getcwd(), "src/files/prompts", "endgame.txt"))
wait = None
fund = ""

def bobo_tag(mess):
    global user_id
    if mess == "BOBO MO":
        mess = 'BOBO MO <@{!s}>'.format(user_id)
        return mess
    return mess


def find_Bobo(words):
    for word in words:
        if word == "bobo":
            return True
    return False


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


@client.event
async def on_ready():
    db.connect()
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(
        len(set(client.get_all_members()))) + ' users')
    # type 1 = playing, 2 = listeningto, 3 = watching
    return await client.change_presence(game=discord.Game(name='anal child porn while fucking children', type=3))


@client.event
async def on_message(message):
    global user_id
    user_id = message.author.id
    await client.process_commands(message)
    words = message.content.lower().split()
    #if (user_id in mudae_ids and message.embeds):
    #    await client.add_reaction(message, u"\u2B05")
    #    await client.add_reaction(message, u"\u27A1")
    #    await asyncio.sleep(3)
    #    await client.add_reaction(message, 	u"\U0001F496")
    if user_id != client.user.id and message.author.server.id != "607181202922799135":
        if message.content.startswith('v!8ball'):
            if len(words) == 1:
                await client.send_message(message.channel, "THAT AIN'T A FUCKING QUESTION FFS")
            else:
                await client.send_message(message.channel, random.choice(ball_replies))
        elif message.content.lower() == "good vade":
            await client.send_file(message.channel, 'src/pics/vadesmile.jpg')
        elif message.content.lower() == "bad vade":
            await client.send_file(message.channel, 'src/pics/badvade.jpg')
        elif find_Bobo(words):
            await client.send_message(message.channel, bobo_tag("BOBO MO"))
        elif random.randint(1, 100) <= 3:
            msg = random.choice(messages)
            await client.send_message(message.channel, bobo_tag(msg))

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension('commands.{}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(
                'commands.{}'.format(extension), exc))
    client.run(os.environ['VadeBot_Token'])
