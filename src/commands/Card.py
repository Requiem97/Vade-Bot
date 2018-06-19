import discord
from discord.ext import commands
from src.commands import VadeDeets

class Card:
    "Views some cards saved before the death of Bully Bot"
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def card (self, cmd, card):
        "v!card view [card] to view specified card\nv!card list to view all cards"
        if cmd != "view" and cmd != "list" :
            await self.bot.say("BAWAL YAN BOBO!")
        elif cmd == "view":
            if card == None:
                pass
            else:
                await self.bot.upload(VadeDeets.cardList[VadeDeets.cardMap.index(card)])
        elif cmd == "list":
            commonCards = [x.endswith("1") for x in VadeDeets.cardMap]
            uncommonCards = [x.endswith("2") for x in VadeDeets.cardMap]
            rareCards = [x.endswith("3") for x in VadeDeets.cardMap]
            specialCards = [x.endswith("4") for x in VadeDeets.cardMap]
            await self.bot.say("__**Common Cards**__\n", (x for x in commonCards))

def setup(bot):
    bot.add_cog(Card(bot))