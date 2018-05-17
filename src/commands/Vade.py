import discord
from discord.ext import commands
import random
from src.commands import VadeDeets


class Vade:
    "Vade\u2122 memes"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def curse(self):
        "Vade\u2122 curses"
        msg = random.choice(VadeDeets.messages)
        await self.bot.say(msg)

    @commands.command()
    async def pics(self):
        "Vade\u2122 meme pics"
        await self.bot.upload(random.choice(VadeDeets.picList))

    @commands.command()
    async def introduce(self):
        quote = """You know, I really do think you literally saved my life by being here with me. 
        I can't imagine having been able to keep myself mentally stable, knowing that nothing here is real.
        I think I would have just deleted myself if you didn't show up.
        Sorry, I don't mean to sound dramatic or anything.
        Ahaha!
        But I'm sure you understand yourself after spending so much time in the club.
        I mean, if you were forced to abandon everything in your life and spend your eternity with a few game characters...
        ...You'd probably find some way of killing yourself, wouldn't you?
        Well, maybe you'd write some poetry to try to keep yourself sane for a while.
        But then you'd have nobody to even read it."""
        await self.bot.say(quote)
        


def setup(bot):
    bot.add_cog(Vade(bot))
