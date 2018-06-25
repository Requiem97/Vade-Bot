import discord, random, datetime
from discord.ext import commands
from src.commands import VadeDeets
from src.db import connect

class Card:
    "Views some cards saved before the death of Bully Bot"
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self):
        "Daily giveaway using the NOHK fund"
        date = datetime.datetime.now()
        amount = random.randint(20,30)
        if connect.hasData(VadeDeets.userID):
            if connect.canUse(VadeDeets.userID):
                connect.uploadData(VadeDeets.userID, amount, date)
                await self.bot.say("You got " + str(amount) + " Php from the fund.")
            else:
                await self.bot.say("Please try again in " + VadeDeets.wait)
        else: 
            connect.createData(VadeDeets.userID, amount, date)
            await self.bot.say("You got " + str(amount) + " Php from the fund.")
    
    @commands.group(pass_context=True)
    async def card (self, ctx):
        "use v!help card to view more"
        if ctx.invoked_subcommand is None:
            await self.bot.say("BAWAL YAN BOBO!")

            
    @card.command()
    async def view(self, card):
        "v!card view [card] to view the specified card, provided it's in the list"
        if card == None:
            pass
        else:
            await self.bot.upload(VadeDeets.cardList[VadeDeets.cardMap.index(card.lower())])

    @card.command()
    async def list(self):
        "v!card list to view the list of availbale card for viewing"
        commonCards = [card for card in VadeDeets.cardMap if "1" in card]
        uncommonCards = [card for card in VadeDeets.cardMap if "2" in card]
        rareCards = [card for card in VadeDeets.cardMap if "3" in card]
        specialCards = [card for card in VadeDeets.cardMap if "4" in card]
        commonCards.sort()
        uncommonCards.sort()
        rareCards.sort()
        specialCards.sort()
        commonText = "__**Common Cards**__\n" + str(commonCards).strip("[]")
        uncommonText = "__**Uncommon Cards**__\n" + str(uncommonCards).strip("[]")
        rareText = "__**Rare Cards**__\n" + str(rareCards).strip("[]")
        specialText = "__**Special Cards**__\n" + str(specialCards).strip("[]")
        message = (commonText + "\n\n" + uncommonText + "\n\n" + rareText + "\n\n" + specialText).replace("'","")
        await self.bot.say(message)


def setup(bot):
    bot.add_cog(Card(bot))