import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup


class Rainbow6:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def r6(self, user):
        "Views general Rainbow 6 Siege stats of specified user"
        url = 'https://r6.tracker.network/profile/pc/{}'.format(user.lower())
        request = requests.get(url)
        scrape = BeautifulSoup(request.text, 'html.parser')
        if request.status_code == 200:
            #About Data
            user = scrape.select("div.trn-profile-header.trn-card > div > h1 > span")
            rank = scrape.select(
                "div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__info > div:nth-child(3) > div.trn-text--dimmed.trn-text--center")
            profile_pic = scrape.select(
                "div.trn-profile-header.trn-card > div > div.trn-profile-header__avatar.trn-roundavatar.trn-roundavatar--white > img")
            level = scrape.select("div.trn-card__content.trn-card--light.trn-defstats-grid > div:nth-child(1) > div > div.trn-defstat__value")
            pvp_time_played = scrape.find("div", { "data-stat" : "PVPTimePlayed" })

            #Win/Loss data
            pvp_wins = scrape.find("div", {"data-stat": "PVPMatchesWon"})
            pvp_loses = scrape.find("div", {"data-stat": "PVPMatchesLost"})
            pvp_wl_ratio = scrape.find("div", {"data-stat": "PVPWLRatio"})

            #Kill/Death data
            pvp_kills = scrape.find("div", {"data-stat": "PVPKills"})
            pvp_deaths = scrape.find("div", {"data-stat": "PVPDeaths"})
            pvp_kd = scrape.find("div", {"data-stat": "PVPKDRatio"})
            pvp_headshots = scrape.find("div", {"data-stat": "PVPHeadshots"})
            pvp_melee = scrape.find("div", {"data-stat": "PVPMeleeKills"})
            pvp_blind = scrape.find("div", {"data-stat": "PVPBlindKills"})

            embed = discord.Embed(title="General Rainbow Six Siege Stats", colour=discord.Colour(0x903c31), url=url)
            embed.set_thumbnail(url=profile_pic[0]['src'])
            embed.set_author(name=user[0].text.strip(),
                             icon_url=profile_pic[0]['src'])
            embed.set_footer(text="Stats taken from r6.tracker.network")

            #About Field
            if rank:
                embed.add_field(name="About", 
                                value="**Level:** {}\n".format(level[0].text.strip()) \
                                    +"**Time Played:** {}\n".format(pvp_time_played.text.strip()) \
                                    +"**Rank:** {}".format(rank[0].text.strip()))

            else:
                embed.add_field(name="About", 
                                value="**Level:** {}\n".format(level[0].text.strip())  \
                                    +"**Time Played:** {}\n".format(pvp_time_played.text.strip()))

            #Win/Loss field
            embed.add_field(name="Win/Loss",
                            value="**Wins:** {}\n".format(pvp_wins.text.strip()) \
                                + "**Loses:** {}\n".format(pvp_loses.text.strip()) \
                                + "**W/R:** {}".format(pvp_wl_ratio.text.strip()), 
                            inline=True)
            
            #Kill/Death field
            embed.add_field(name="Kills/Deaths",
                            value="**Kills:** {}\n".format(pvp_kills.text.strip()) \
                                + "**Deaths:** {}\n".format(pvp_deaths.text.strip()) \
                                + "**K/D:** {}\n".format(pvp_kd.text.strip()) \
                                + "**Headshots:** {}\n".format(pvp_headshots.text.strip()) \
                                + "**Melee Kills:** {}\n".format(pvp_melee.text.strip()) \
                                + "**Blind Kills:** {}".format(pvp_blind.text.strip()), 
                            inline=True)
            await self.bot.say(embed=embed)
        elif request.status_code == 404:
            await self.bot.say("User does not exist")
        else:
            await self.bot.say("Some error has occured")

def setup(bot):
    bot.add_cog(Rainbow6(bot))