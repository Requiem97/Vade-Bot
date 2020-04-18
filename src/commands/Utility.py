import random
import discord
from discord.ext import commands

class Utility(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.ball_replies = []
        with open("src/files/8ballReplies.txt") as file:
            self.ball_replies = [line.strip() for line in file]

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

    @commands.command(name='8ball')
    async def _8ball(self, ctx, question = None):
        "Ask Vade a question"
        if question is None:
            await ctx.send("THAT AIN'T A FUCKING QUESTION FFS")
        else:
            await ctx.send(random.choice(self.ball_replies))

def setup(bot):
    bot.add_cog(Utility(bot))
