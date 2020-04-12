import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup


class Rainbow6:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def r6(self, ctx, user=None):
        "Views General Rainbow 6 Siege stats of specified user"
        if ctx.invoked_subcommand is None and user is not None:
            url = 'https://r6.tracker.network/profile/pc/{}'.format(user.lower())
            scrape, status_code = self.get_scrapper(url)
            if status_code == 200:
                user, rank, profile_pic, level = self.get_profile_data(scrape)

                #Win/Loss data
                pvp_time_played = scrape.find("div", { "data-stat" : "PVPTimePlayed" })
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

                embed = discord.Embed(title="General Rainbow Six Siege Stats", colour=discord.Colour(0x903c31))
                embed.set_thumbnail(url=profile_pic[0]['src'])
                embed.set_author(name=user[0].text.strip(),
                                url=url,
                                icon_url=profile_pic[0]['src'])
                embed.set_footer(text="Stats taken from r6.tracker.network")

                #About Field
                if rank:
                    embed.add_field(name="About", 
                                    value="**Level:** {}\n".format(level[0].text.strip()) \
                                        +"**Time Played:** {}\n".format(pvp_time_played.text.strip()) \
                                        +"**Rank:** {}\n".format(rank[0].text.strip()))

                else:
                    embed.add_field(name="About", 
                                    value="**Level:** {}\n".format(level[0].text.strip())  \
                                        +"**Time Played:** {}\n".format(pvp_time_played.text.strip()))

                #Win/Loss field
                embed.add_field(name="Win/Loss",
                                value="**Wins:** {}\n".format(pvp_wins.text.strip()) \
                                    + "**Loses:** {}\n".format(pvp_loses.text.strip()) \
                                    + "**W/R:** {}\n".format(pvp_wl_ratio.text.strip()), 
                                inline=True)
                
                #Kill/Death field
                embed.add_field(name="Kills/Deaths",
                                value="**Kills:** {}\n".format(pvp_kills.text.strip()) \
                                    + "**Deaths:** {}\n".format(pvp_deaths.text.strip()) \
                                    + "**K/D:** {}\n".format(pvp_kd.text.strip()) \
                                    + "**Headshots:** {}\n".format(pvp_headshots.text.strip()) \
                                    + "**Melee Kills:** {}\n".format(pvp_melee.text.strip()) \
                                    + "**Blind Kills:** {}\n".format(pvp_blind.text.strip()), 
                                inline=True)
                await self.bot.say(embed=embed)
            elif status_code == 404:
                await self.bot.say("User does not exist")
            else:
                await self.bot.say("Some error has occured")
        else:
            await self.bot.say("__**R6 commands**__\n" +
                    "`v!r6 [user]` - views General R6 stats of the user.\n" +
                    "`v!r6 ranked [user]` - views ranked R6 stats of the user.\n\n"
                )
    
    @r6.command()
    async def ranked(self, user=None):
        "Views Ranked Rainbow 6 Siege stats of specified user"
        if user is None:
            await self.bot.say("Please specify a user")
        else:
            pass

def get_scrapper(self, url):
    request = requests.get(url)
    return BeautifulSoup(request.text, 'html.parser'), request.status_code

def get_profile_data(self, scrape):
    #About Data
    user = scrape.select("div.trn-profile-header.trn-card > div > h1 > span")[0].get_text()
    rank = scrape.select(
        "div.trn-scont.trn-scont--swap > div.trn-scont__content > div:nth-child(4) > div.r6-season-list > div > div.r6-season__info > div:nth-child(3) > div.trn-text--dimmed.trn-text--center"
    )[0].get_text()
    profile_pic = scrape.select(
        "div.trn-profile-header.trn-card > div > div.trn-profile-header__avatar.trn-roundavatar.trn-roundavatar--white > img"
    )[0].get_text()
    level = scrape.select(
        "div.trn-card__content.trn-card--light.trn-defstats-grid > div:nth-child(1) > div > div.trn-defstat__value"
    )[0].get_text()
    return user, rank, profile_pic, level

def setup(bot):
    bot.add_cog(Rainbow6(bot))