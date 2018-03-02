import discord
from discord.ext import commands

class Utility():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bros(self, user: discord.User = None):
        "What Vade should prioritise"
        try:
            if user:
                await self.bot.say( 'Bros before hoes <@{!s}>'.format( user.id ) )
            else:
                await self.bot.say( 'Bros before hoes' )
        except:
            await self.bot.say( 'Bros before hoes' )
    
    @commands.command()
    async def ping(self):
        "Pings to all game servers in existence"
        await self.bot.say( "I'M LAGGING FUCK MY LIFE" )

def setup(bot):
    bot.add_cog(Utility(bot))