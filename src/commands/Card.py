import discord
from discord.ext import commands
from src.commands import VadeDeets

class Card:
    "Views some cards saved before the death of Bully Bot"
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(pass_context=True)
    async def card (self, ctx):
        "v!card view [card] to view specified card, and v!card list to view all cards"
        if ctx.invoked_subcommand is None:
            await self.bot.say("BAWAL YAN BOBO!")

            
    @card.command()
    async def view(self, card):
        if card == None:
            pass
        else:
            await self.bot.upload(VadeDeets.cardList[VadeDeets.cardMap.index(card)])
    @card.command()
    async def list(self):
        commonCards = [x.endswith("1") for x in VadeDeets.cardMap]
        uncommonCards = [x.endswith("2") for x in VadeDeets.cardMap]
        rareCards = [x.endswith("3") for x in VadeDeets.cardMap]
        specialCards = [x.endswith("4") for x in VadeDeets.cardMap]
        commonText = "__**Common Cards**__\n" + str(commonCards).strip("['']")
        await self.bot.say(commonText)


def setup(bot):
    bot.add_cog(Card(bot))