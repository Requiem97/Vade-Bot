import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
class Rainbow6:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def r6(self, user):
        url = 'https://r6.tracker.network/profile/pc/{}'.format(user.lower())
        request = requests.get(url)
        scrape = BeautifulSoup(request.text, 'html.parser')
        if request.status_code == 200: 
            rank = scrape.select("#profile > div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__info > div:nth-child(3) > div.trn-text--dimmed.trn-text--center")
            profile_pic = scrape.select("#profile > div.trn-profile-header.trn-card > div > div.trn-profile-header__avatar.trn-roundavatar.trn-roundavatar--white > img")[0]['src']
            wins = scrape.find("div", { "data-stat" : "PVPMatchesWon" })
            win_ratio = scrape.find("div", { "data-stat" : "PVPWLRatio" })
            pvp_kills = scrape.find("div", { "data-stat" : "PVPKills" })
            pvp_kd = scrape.find("div", { "data-stat" : "PVPKDRatio" })
            loses = scrape.find("div", { "data-stat" : "PVPMatchesLost" })
            embed = discord.Embed(title="{!s} Rainbow 6 Siege stats".format(user), colour=discord.Colour(0x4e07b3), url=url, description="These are the general stats of {!s}  in Rainbow Six Siege".format(user))
            embed.set_thumbnail(url=profile_pic)
            if rank:
                embed.add_field(name="Rank", value=rank[0].text)
            embed.add_field(name="Wins", value=wins.text, inline=True)
            embed.add_field(name="Loses", value=loses.text, inline=True)
            embed.add_field(name="Win Ratio", value=win_ratio.text)
            embed.add_field(name="Kills", value=pvp_kills.text, inline=True)
            embed.add_field(name="K/D", value=pvp_kd.text, inline=True)
            await self.bot.say(embed=embed)
        elif request.status_code == 404:
            print("user does not exist")
            await self.bot.say("User does not exist")
        else:
            await self.bot.say("Some error has occured")

def setup(bot):
    bot.add_cog(Rainbow6(bot))