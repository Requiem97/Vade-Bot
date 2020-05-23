import random
import discord
from discord.ext import commands

class Utility(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bros(self, ctx, user: discord.User = None):
        "What Vade should prioritise"
        try:
            if user:
                await ctx.send('Bros before hoes <@{!s}>'.format(user.id))
            else:
                await ctx.send('Bros before hoes')
        except:
            await ctx.send('Bros before hoes')

    @commands.command()
    async def ping(self, ctx):
        "Pings to all game servers in existence"
        await ctx.send("I'M LAGGING FUCK MY LIFE")

def setup(bot):
    bot.add_cog(Utility(bot))
