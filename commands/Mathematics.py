import discord
import logging
from discord.ext import commands

class Mathematics(commands.Cog):
    "Does some Math stuff"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, x, y):
        "Adds some shit"
        try:
            z = float(x) + float(y)
            await ctx.send('{:0.2f} + {:0.2f} is {:0.2f} \nQuick mafs'.format(float(x), float(y), float(z)))
        except ValueError:
            await ctx.send("That ain't a number ffs")

    @commands.command()
    async def multiply(self, ctx, x, y):
        "Multiplies some shit"
        try:
            z = float(x) * float(y)
            await ctx.send('{:0.2f} * {:0.2f} is {:0.2f} \nQuick mafs'.format(float(x), float(y), float(z)))
        except ValueError:
            await ctx.send("That ain't a number ffs")

    @commands.command()
    async def subtract(self, ctx, x, y):
        "Subtracts some shit"
        try:
            z = float(x) - float(y)
            await ctx.send('{:0.2f} - {:0.2f} is {:0.2f} \nQuick mafs'.format(float(x), float(y), float(z)))
        except ValueError:
            await ctx.send("That ain't a number ffs")

    @commands.command()
    async def divide(self, ctx, x, y):
        "Divides some shit"
        try:
            z = float(x) / float(y)
            await ctx.send('{:0.2f} / {:0.2f} is {:0.2f} \nQuick mafs'.format(float(x), float(y), float(z)))
        except ValueError:
            await ctx.send("That ain't a number ffs")
        except ZeroDivisionError:
            await ctx.send('BOBO MO <@{!s}> DI PWEDE YAN'.format(ctx.message.author.id))


def setup(bot):
    bot.add_cog(Mathematics(bot))
