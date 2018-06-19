import discord
from discord.ext import commands
from src.commands import VadeDeets

class Card:
    "Views some cards saved before the death of Bully Bot"
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def card (self, cmd, card):
        if cmd != "view":
            await self.bot.say("BAWAL YAN BOBO!")
        elif card == None:
            pass
        else:
            await self.bot.upload(VadeDeets.cardList[VadeDeets.cardMap.index(card)])

def setup(bot):
    bot.add_cog(Card(bot))