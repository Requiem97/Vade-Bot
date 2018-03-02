import os
import random

import discord
from discord.ext.commands import Bot

client = Bot( description="FUCK THIS SHIT", command_prefix="v!", pm_help=False )
messages = []
with open( "src/curse.txt" ) as file:
    messages = [line.strip() for line in file]
picList = []
for file in os.listdir( "src/" ):
    if file.endswith( ".png" ) or file.endswith( ".jpg" ):
        picList.append( 'src/{}'.format(file) )
ballReplies=[]
with open( "src/8ballReplies.txt" ) as file:
    ballReplies = [line.strip() for line in file]
UserID = ""
channel = ""
extensions=['Utility','Mathematics']


@client.event
async def on_ready():
    print( 'Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len( client.servers ) ) + ' servers | Connected to ' + str(
        len( set( client.get_all_members() ) ) ) + ' users' )
    return await client.change_presence( game=discord.Game( name='SOME SHITTY GAME' ) )


@client.event
async def on_message(message):
    global UserID
    global channel
    channel = message.channel
    UserID = message.author.id
    await client.process_commands( message )
    words = message.content.lower().split()
    if UserID != client.user.id:
        if message.content.startswith('v!8ball'):
            if len(words) == 1:
                await client.send_message( message.channel, "THAT AIN'T A FUCKING QUESTION FFS" )
            else:
                await client.send_message( message.channel, random.choice(ballReplies))
        if message.content.lower() == "good vade":
            await client.send_file(message.channel,'src/vadesmile.jpg')
        if message.content.lower() == "bad vade":
            await client.send_file(message.channel,'src/badvade.jpg')
        if findBobo( words ) == True:
            await client.send_message( message.channel, boboTag( "BOBO MO" ) )
        elif random.randint( 1, 100 ) <= 3:
            msg = random.choice( messages )
            await client.send_message( message.channel, boboTag( msg ) )

@client.event
async def on_command_error(self, error):
    pass


@client.command()
async def curse():
    "Vade\u2122 curses"
    msg = random.choice( messages )
    await client.say( boboTag( msg ) )


@client.command()
async def pics():
    "Vade meme pics"
    await client.upload( random.choice( picList ) )


def boboTag(mess):
    if mess == "BOBO MO":
        mess = 'BOBO MO <@{!s}>'.format( UserID )
        return mess
    return mess


def findBobo(words):
    for word in words:
        if word == "bobo":
            return True
    return False

if __name__=='__main__':
    for extension in extensions:
        try:
            client.load_extension('commands.{}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format('commands.{}'.format(extension), exc))
client.run( os.environ['VadeBot_Token'] )
