import os
import random
import discord
from discord.ext.commands import Bot
from src.commands import VadeDeets

client = Bot(description="FUCK THIS SHIT", command_prefix="v!", pm_help=False)
extensions = ['Utility', 'Mathematics', 'Vade', 'Card']

@client.event
async def on_ready():
    print(os.environ['DATABASE_URL'])
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(
        len(set(client.get_all_members()))) + ' users')
    #type 1 = playing, 2 = listeningto, 3 = watching
    return await client.change_presence(game=discord.Game(name='anal child porn while fucking children', type=3))

@client.event
async def on_message(message):
    VadeDeets.userID = message.author.id
    await client.process_commands(message)
    words = message.content.lower().split()
    if VadeDeets.userID != client.user.id:
        if message.content.startswith('v!8ball'):
            if len(words) == 1:
                await client.send_message(message.channel, "THAT AIN'T A FUCKING QUESTION FFS")
            else:
                await client.send_message(message.channel, random.choice(VadeDeets.ballReplies))
        elif message.content.lower() == "good vade":
            await client.send_file(message.channel, 'src/pics/vadesmile.jpg')
        elif message.content.lower() == "bad vade":
            await client.send_file(message.channel, 'src/pics/badvade.jpg')
        elif VadeDeets.findBobo(words):
            await client.send_message(message.channel, VadeDeets.boboTag("BOBO MO"))
        elif random.randint(1, 100) <= 3:
            msg = random.choice(VadeDeets.messages)
            await client.send_message(message.channel, VadeDeets.boboTag(msg))

@client.event
async def on_command_error(self, error):
    pass

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension('commands.{}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(
                'commands.{}'.format(extension), exc))
    client.run(os.environ['VadeBot_Token'])
