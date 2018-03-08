import discord
from discord.ext import commands
import VadeDeets


class Mathematics:
    "Does some Math stuff"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, x, y):
        "Adds some shit"
        try:
            z = float(x) + float(y)
            await self.bot.say('{:0.2f} + {:0.2f} is {:0.2f} \nQuick mafs'.format(float(x), float(y), float(z)))
        except ValueError:
            await self.bot.say("That ain't a number ffs")

    @commands.command()
    async def multiply(self, x, y):
        "Multiplies some shit"
        try:
            z = float(x) * float(y)
            await self.bot.say('{:0.2f} * {:0.2f} is {:0.2f} \nQuick mafs'.format(float(x), float(y), float(z)))
        except ValueError:
            await self.bot.say("That ain't a number ffs")

    @commands.command()
    async def subtract(self, x, y):
        "Subtracts some shit"
        try:
            z = float(x) - float(y)
            await self.bot.say('{:0.2f} - {:0.2f} is {:0.2f} \nQuick mafs'.format(float(x), float(y), float(z)))
        except ValueError:
            await self.bot.say("That ain't a number ffs")

    @commands.command()
    async def divide(self, x, y):
        "Divides some shit"
        try:
            z = float(x) / float(y)
            await self.bot.say('{:0.2f} / {:0.2f} is {:0.2f} \nQuick mafs'.format(float(x), float(y), float(z)))
        except ValueError:
            await self.bot.say("That ain't a number ffs")
        except ZeroDivisionError:
            await self.bot.say('BOBO MO <@{!s}> DI PWEDE YAN'.format(VadeDeets.userID))


def setup(bot):
    bot.add_cog(Mathematics(bot))
