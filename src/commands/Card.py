import discord
from discord.ext import commands
from src.commands import VadeDeets

class Card:
    "Views some cards saved before the death of Bully Bot"
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(pass_context=True)
    async def card (self, ctx):
        "use v!card help to view more"
        if ctx.invoked_subcommand is None:
            await self.bot.say("BAWAL YAN BOBO!")

            
    @card.command()
    async def view(self, card):
        "v!card view [card] to view the specified card, provided it's in the list"
        if card == None:
            pass
        else:
            await self.bot.upload(VadeDeets.cardList[VadeDeets.cardMap.index(card)])

    @card.command()
    async def list(self):
        "v!card list to view the list of availbale card for viewing"
        commonCards = [card for card in VadeDeets.cardMap if "1" in card]
        uncommonCards = [card for card in VadeDeets.cardMap if "2" in card]
        rareCards = [card for card in VadeDeets.cardMap if "3" in card]
        specialCards = [card for card in VadeDeets.cardMap if "4" in card]
        commonText = "__**Common Cards**__\n" + str(commonCards).strip("[]")
        uncommonText = "__**Uncommon Cards**__\n" + str(uncommonCards).strip("[]")
        rareText = "__**Rare Cards**__\n" + str(rareCards).strip("[]")
        specialText = "__**Special Cards**__\n" + str(specialCards).strip("[]")
        message = (commonText + "\n\n" + uncommonText + "\n\n" + rareText + "\n\n" + specialText).replace("'","")
        await self.bot.say(message)


def setup(bot):
    bot.add_cog(Card(bot))