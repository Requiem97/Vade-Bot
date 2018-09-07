import os
import random
import discord
import glob
import datetime
from discord.ext.commands import Bot
from src.util import db

client = Bot(description="FUCK THIS SHIT", command_prefix="v!", pm_help=False)
extensions = ['Utility', 'Mathematics', 'Vade', 'NOHK']

userID = '0'
file_list = glob.glob(os.path.join(os.getcwd(), "src/files/prompts", "*.txt"))
wait = None
fund = ""

def boboTag(mess):
    if mess == "BOBO MO":
        mess = 'BOBO MO <@{!s}>'.format(userID)
        return mess
    return mess


def findBobo(words):
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

picList = []
for file in os.listdir("src/pics"):
    if file.endswith(".png") or file.endswith(".jpg"):
        picList.append('src/pics/{}'.format(file))

cardList = []
for file in os.listdir("src/cards"):
    if file.endswith(".png") or file.endswith(".jpg"):
        cardList.append('src/cards/{}'.format(file))
cardMap = [x.replace("src/cards/", "").replace(".png",
                                               "").replace(".jpg", "").lower() for x in cardList]

ballReplies = []
with open("src/files/8ballReplies.txt") as file:
    ballReplies = [line.strip() for line in file]


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
    global userID
    userID = message.author.id
    await client.process_commands(message)
    words = message.content.lower().split()
    if userID != client.user.id:
        if message.content.startswith('v!8ball'):
            if len(words) == 1:
                await client.send_message(message.channel, "THAT AIN'T A FUCKING QUESTION FFS")
            else:
                await client.send_message(message.channel, random.choice(ballReplies))
        elif message.content.lower() == "good vade":
            await client.send_file(message.channel, 'src/pics/vadesmile.jpg')
        elif message.content.lower() == "bad vade":
            await client.send_file(message.channel, 'src/pics/badvade.jpg')
        elif findBobo(words):
            await client.send_message(message.channel, boboTag("BOBO MO"))
        elif random.randint(1, 100) <= 3:
            msg = random.choice(messages)
            await client.send_message(message.channel, boboTag(msg))

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension('commands.{}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(
                'commands.{}'.format(extension), exc))
    client.run(os.environ['VadeBot_Token'])
