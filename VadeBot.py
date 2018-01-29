import discord
import asyncio
import random
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import os

client = Bot(description="FUCK THIS SHIT", command_prefix="v!", pm_help = False)
command_prefix="v!"
messages=[]
with open("curse.txt") as file:
		messages = [line.strip() for line in file]
picList=[]
for file in os.listdir("."):
	if file.endswith(".png") or file.endswith(".jpg"):
		picList.append(file)
UserID="test"

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	return await client.change_presence(game=discord.Game(name='SOME SHITTY GAME'))

@client.event
async def on_message(message):
	global UserID
	UserID = message.author.id
	await client.process_commands(message)
	words = message.content.lower().split()
	if UserID != client.user.id:
		if random.randint(1,100) <= 3:
			msg = random.choice(messages)
			await client.send_message(message.channel, boboTag(msg))
		if findBobo(words) == True:
			await client.send_message(message.channel, boboTag("BOBO MO"))

@client.command()
async def ping():
	await client.say("I'M LAGGING FUCK MY LIFE")	

@client.command()
async def curse():
	msg = random.choice(messages)
	await client.say(boboTag(msg))

@client.command()
async def pics():
	await client.upload(random.choice(picList))

@client.command()
async def add(x, y):
	try:
		z = int(x)+int(y)
		await client.say('{:d} + {:d} is {:d} \nQuick mafs'.format(int(x), int(y), int(z)))
	except ValueError:
		await client.say("That ain't a number ffs")

@client.command()
async def multiply(x, y):
	try:
		z = int(x)*int(y)
		await client.say('{:d} * {:d} is {:d} \nQuick mafs'.format(int(x), int(y), int(z)))
	except ValueError:
		await client.say("That ain't a number ffs")

@client.command()
async def subtract(x, y):
	try:
		z = int(x)-int(y)
		await client.say('{:d} - {:d} is {:d} \nQuick mafs'.format(int(x), int(y), int(z)))
	except ValueError:
		await client.say("That ain't a number ffs")
		
@client.command()
async def divide(x, y):
	try:
		z = float(x)/float(y)
		await client.say('{:0.1f} / {:0.1f} is {:0.1f} \nQuick mafs'.format(float(x), float(y), float(z)))
	except ValueError:
		await client.say("That ain't a number ffs")
	except ZeroDivisionError:
		await client.say('BOBO MO <@{!s}> DI PWEDE YAN'.format(UserID))

def boboTag(mess):
	if mess=="BOBO MO":
		mess='BOBO MO <@{!s}>'.format(UserID)
		return mess
	return mess
	
def findBobo(words):
	for word in words:
		if word == "bobo":
			return True
	return False
	
client.run(os.environ['VadeBot_Token'])

