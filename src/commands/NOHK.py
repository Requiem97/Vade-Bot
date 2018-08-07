import datetime
import discord
import gspread
import os
import json
import random
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials
from src.commands import VadeDeets
from src.util import db


class NOHK:
    "Views some cards saved before the death of Bully Bot"

    def __init__(self, bot):
        self.bot = bot
        self.set_credentials()

    @commands.command()
    async def daily(self):
        "Daily giveaway using the NOHK fund"
        date = datetime.datetime.now()
        amount = random.randint(20, 30)
        if db.hasData(VadeDeets.userID):
            if db.canUse(VadeDeets.userID):
                db.uploadData(VadeDeets.userID, amount, date)
                await self.bot.say("You got " + str(amount) + " Php from the fund.")
            else:
                wait = VadeDeets.wait.split(":")
                await self.bot.say("Please try again in " + wait[0] + " hours " + wait[1] + " minutes and " + wait[2] + " seconds.")
        else:
            db.createData(VadeDeets.userID, amount, date)
            await self.bot.say("You got " + str(amount) + " Php from the fund.")

    @commands.command()
    async def balance(self):
        "Get personal fund balance"
        db.getFund(VadeDeets.userID)
        fund = db.getFund(VadeDeets.userID)
        await self.bot.say("You have " + str(fund) + " Php.")

    @commands.group(pass_context=True)
    async def card(self, ctx):
        "use v!help card to view more"
        if ctx.invoked_subcommand is None:
            await self.bot.say("BAWAL YAN BOBO!")

    @card.command()
    async def view(self, card):
        "v!card view [card] to view the specified card, provided it's in the list"
        if card == None:
            pass
        else:
            await self.bot.upload(VadeDeets.cardList[VadeDeets.cardMap.index(card.lower())])

    @card.command()
    async def list(self):
        "v!card list to view the list of availbale card for viewing"
        cardList = VadeDeets.cardMap
        #cardList.sort()
        commonCards = [card.title()
                       for card in cardList if "1" in card]
        uncommonCards = [card.title()
                         for card in cardList if "2" in card]
        rareCards = [card.title()
                     for card in cardList if "3" in card]
        specialCards = [card.title()
                        for card in cardList if "4" in card]
        commonText = "__**Common Cards**__\n" + str(commonCards).strip("[]")
        uncommonText = "__**Uncommon Cards**__\n" + \
            str(uncommonCards).strip("[]")
        rareText = "__**Rare Cards**__\n" + str(rareCards).strip("[]")
        specialText = "__**Special Cards**__\n" + str(specialCards).strip("[]")
        message = (commonText + "\n\n" + uncommonText + "\n\n" +
                   rareText + "\n\n" + specialText).replace("'", "")
        await self.bot.say(message)

    @commands.group(pass_context=True)
    async def fund(self, ctx):
        "NOHK fund-related command group. v!help fund to view more"
        if ctx.invoked_subcommand == None:
            await self.bot.say("__**NOHK Fund commands**__\n" +
                               "`v!fund utang [member]` - views debt of specified member.\n" +
                               "`v!fund total` - views the current on hand amount.\n\n" +
                               "use `v!balance`  to view your v!daily total")

    @fund.command()
    async def utang(self, member=None):
        "views debt of a sepcified member"

        if member == None:
            await self.bot.say("Specify a fund subscriber dumbass")
            return
        try:
            val = self.get_amount(member)
            await self.bot.say(member + "'s current debt is " + str(val))
        except gspread.exceptions.APIError:
            self.set_credentials()
            val = self.get_amount(member)
            await self.bot.say(member + "'s current debt is " + str(val))
            #await self.bot.say("Error with Google API key. Please contact the developer <@{!s}>".format(os.environ['DEV_ID']))
        except:
            await self.bot.say("SUMALI KA MUNA SA COLLECTION GAGO!")

    @fund.command()
    async def total(self):
        "views the current on hand ammount."
        sheet = self.file.open_by_key(os.environ['Sheet_ID_2018'])
        worksheet = sheet.get_worksheet(0)
        val = worksheet.cell(25, 1).value
        await self.bot.say("Current amount on hand is " + str(val) + " Php.")

    def set_credentials(self):
        self.scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        self.service_account_info = json.loads(os.environ['Google_Key'])
        self.credentials = ServiceAccountCredentials._from_parsed_json_keyfile(
            self.service_account_info, self.scope)
        self.file = gspread.authorize(self.credentials)

    def get_amount(self, member):
        sheet = self.file.open_by_key(os.environ['Sheet_ID_2017'] if member.lower() == 'harold'
                                      else os.environ['Sheet_ID_2018'])
        worksheet = sheet.get_worksheet(0)
        users = {
            'alkaeid': 14,
            'arvin': 15,
            'marx': 16,
            'otacom': 17,
            'harold': 17,
            'requiem': 18,
            'rich': 19,
            'ruo': 20,
            'vade': 21
        }
        num = users[member.lower()]
        return worksheet.cell(num, 2).value


def setup(bot):
    bot.add_cog(NOHK(bot))
