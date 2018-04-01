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
        for line in VadeDeets.messages:
            await self.bot.say(line)

    @commands.command()
    async def pics(self):
        "Vade\u2122 meme pics"
        await self.bot.upload(random.choice(VadeDeets.picList))


def setup(bot):
    bot.add_cog(Vade(bot))
