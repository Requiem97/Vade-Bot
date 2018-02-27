import os
import random

import discord
from discord.ext.commands import Bot


client = Bot( description="FUCK THIS SHIT", command_prefix="v!", pm_help=False )
command_prefix = "v!"
messages = []
with open( "curse.txt" ) as file:
    messages = [line.strip() for line in file]
picList = []
for file in os.listdir( "." ):
    if file.endswith( ".png" ) or file.endswith( ".jpg" ):
        picList.append( file )
ballReplies=[]
with open( "8ballReplies.txt" ) as file:
    ballReplies = [line.strip() for line in file]
UserID = ""
channel = ""


@client.event
async def on_ready():
    print( 'Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len( client.servers ) ) + ' servers | Connected to ' + str(
        len( set( client.get_all_members() ) ) ) + ' users' )
    return await client.change_presence( game=discord.Game( name='with her feelings' ) )


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
            await client.send_file(message.channel,'vadesmile.jpg')
        if message.content.lower() == "bad vade":
            await client.send_file(message.channel,'badvade.jpg')
        if findBobo( words ) == True:
            await client.send_message( message.channel, boboTag( "BOBO MO" ) )
        elif random.randint( 1, 100 ) <= 10:
            msg = random.choice( messages )
            await client.send_message( message.channel, boboTag( msg ) )


@client.event
async def on_command_error(self, error):
    pass


@client.command()
async def ping():
    await client.say( "I'M LAGGING FUCK MY LIFE" )


@client.command()
async def curse():
    msg = random.choice( messages )
    await client.say( boboTag( msg ) )


@client.command()
async def pics():
    await client.upload( random.choice( picList ) )


@client.command()
async def add(x, y):
    try:
        z = int( x ) + int( y )
        await client.say( '{:d} + {:d} is {:d} \nQuick mafs'.format( int( x ), int( y ), int( z ) ) )
    except ValueError:
        await client.say( "That ain't a number ffs" )


@client.command()
async def multiply(x, y):
    try:
        z = int( x ) * int( y )
        await client.say( '{:d} * {:d} is {:d} \nQuick mafs'.format( int( x ), int( y ), int( z ) ) )
    except ValueError:
        await client.say( "That ain't a number ffs" )


@client.command()
async def subtract(x, y):
    try:
        z = int( x ) - int( y )
        await client.say( '{:d} - {:d} is {:d} \nQuick mafs'.format( int( x ), int( y ), int( z ) ) )
    except ValueError:
        await client.say( "That ain't a number ffs" )


@client.command()
async def divide(x, y):
    try:
        z = float( x ) / float( y )
        await client.say( '{:0.1f} / {:0.1f} is {:0.1f} \nQuick mafs'.format( float( x ), float( y ), float( z ) ) )
    except ValueError:
        await client.say( "That ain't a number ffs" )
    except ZeroDivisionError:
        await client.say( 'BOBO MO <@{!s}> DI PWEDE YAN'.format( UserID ) )


@client.command()
async def bros(user: discord.User = None):
    try:
        if user:
            await client.say( 'Bros before hoes <@{!s}>'.format( user.id ) )
        else:
            await client.say( 'Bros before hoes' )
    except:
        await client.say( 'Bros before hoes' )


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


client.run(os.environ['VadeBot_Token'])

