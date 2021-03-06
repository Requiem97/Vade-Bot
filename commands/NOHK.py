import datetime
import discord
import gspread
import logging
import os
import json
import random
import VadeBot as vade_bot
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials
from util import db


class NOHK(commands.Cog):
    "Views some cards saved before the death of Bully Bot"

    def __init__(self, bot):
        self.bot = bot
        self.set_credentials()

    @commands.command()
    async def daily(self, ctx):
        "Daily giveaway using the NOHK fund"
        date = datetime.datetime.now()
        amount = random.randint(20, 30)
        if db.has_data(ctx.message.author.id):
            if db.can_use(ctx.message.author.id):
                db.upload_data(ctx.message.author.id, amount, date)
                await ctx.send("You got " + str(amount) + " Php from the fund.")
            else:
                wait = vade_bot.wait.split(":")
                await ctx.send("Please try again in " + wait[0] + " hours " + wait[1] + " minutes and " + wait[2] + " seconds.")
        else:
            db.create_data(ctx.message.author.id, amount, date)
            await ctx.send("You got " + str(amount) + " Php from the fund.")

    @commands.command()
    async def balance(self, ctx):
        "Get personal fund balance"
        print(ctx.message.author.id)
        fund = db.get_fund(ctx.message.author.id)
        await ctx.send("You have " + str(fund) + " Php.")

    @commands.group()
    async def card(self, ctx):
        "use v!help card to view more"
        if ctx.invoked_subcommand is None:
            await ctx.send("BAWAL YAN BOBO!")

    @card.command()
    async def view(self, ctx, card):
        "v!card view [card] to view the specified card, provided it's in the list"
        if card == None:
            pass
        else:
            await ctx.send(file=discord.File(vade_bot.card_list[vade_bot.card_map.index(card.lower())]))

    @card.command()
    async def list(self, ctx):
        "v!card list to view the list of availbale card for viewing"
        card_list = vade_bot.card_map
        common_cards = [card.title()
                        for card in card_list if "1" in card]
        uncommon_cards = [card.title()
                          for card in card_list if "2" in card]
        rare_cards = [card.title()
                      for card in card_list if "3" in card]
        special_cards = [card.title()
                         for card in card_list if "4" in card]
        common_cards.sort()
        uncommon_cards.sort()
        rare_cards.sort()
        special_cards.sort()
        common_text = "__**Common Cards**__\n" + str(common_cards).strip("[]")
        uncommon_text = "__**Uncommon Cards**__\n" + \
            str(uncommon_cards).strip("[]")
        rare_text = "__**Rare Cards**__\n" + str(rare_cards).strip("[]")
        special_text = "__**Special Cards**__\n" + \
            str(special_cards).strip("[]")
        message = (common_text + "\n\n" + uncommon_text + "\n\n" +
                   rare_text + "\n\n" + special_text).replace("'", "")
        await ctx.send(message)

    @commands.group()
    async def fund(self, ctx):
        "NOHK fund-related command group. v!help fund to view more"
        if ctx.invoked_subcommand == None:
            await ctx.send("__**NOHK Fund commands**__\n" +
                               "`v!fund utang [member]` - views debt of specified member.\n" +
                               "`v!fund total` - views the current on hand amount.\n\n" +
                               "use `v!balance`  to view your v!daily total")

    @fund.command()
    async def utang(self, ctx,  member=None):
        "views debt of a sepcified member"

        if member == None:
            await ctx.send("Specify a fund subscriber dumbass")
            return
        try:
            val = self.get_amount(member)
            await ctx.send(member + "'s current debt is " + str(val))
        except gspread.exceptions.APIError:
            self.set_credentials()
            val = self.get_amount(member)
            await ctx.send(member + "'s current debt is " + str(val))
        except:
            await ctx.send("SUMALI KA MUNA SA COLLECTION GAGO!")

    @fund.command()
    async def total(self, ctx):
        "views the current on hand ammount."
        try:
            val = self.get_fund_total()
        except gspread.exceptions.APIError:
            self.set_credentials()
            val = self.get_fund_total()
        await ctx.send("Current amount on hand is " + str(val) + " Php.")

    @commands.group()
    async def contacts(self, ctx):
        "NOHK contact number-related command group. v!help contacts to view more"
        if ctx.invoked_subcommand == None:
            await ctx.send("__**NOHK Contacts commands**__\n" +
                               "`v!contacts update [number]` - updates contact number.\n" +
                               "`v!contacts get [user]` - gets contact number of user.\n\n")

    @contacts.command()
    async def update(self, ctx, number):
        "Updates your contact number"
        try:
            db.update_number(ctx.message.author.id, ctx.message.guild.id, number)
            await ctx.send("Number updated")
        except Exception as e:
            logging.error('{}: {}'.format(type(e).__name__, e))
            await ctx.send("A fucking error has occurred")
    
    @contacts.command()
    async def get(self, ctx, user: discord.User):
        "Gets the contact number of a user"
        try:
            contact = db.get_number(user.id, ctx.message.guild.id)
            if (contact == "no number"):
                await ctx.send("<@{!s}> has no saved number".format(user.id))
            else:
                await ctx.send(("<@{!s}>'s number is " + str(contact)).format(user.id))
        except Exception as e:
            logging.error('{}: {}'.format(type(e).__name__, e))
            await ctx.send("A fucking error has occurred")


    def set_credentials(self):
        self.scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        self.service_account_info = json.loads(os.environ['Google_Key'])
        self.credentials = ServiceAccountCredentials._from_parsed_json_keyfile(
            self.service_account_info, self.scope)
        self.file = gspread.authorize(self.credentials)

    def get_amount(self, member):
        key = {
            "alkaeid":os.environ['Sheet_ID_2018'],
            "harold":os.environ['Sheet_ID_2017'],
            "otacom":os.environ['Sheet_ID_2018'],
            "requiem":os.environ['Sheet_ID_2018'],
            "tj":os.environ['Sheet_ID_2017']
        }
        sheet = self.file.open_by_key(key.get(member.lower(), os.environ['Sheet_ID_2019']))
        worksheet = sheet.get_worksheet(0)
        users = {
            'alkaeid': 14,
            'arvin': 12,
            'marx': 13,
            'otacom': 17,
            'harold': 17,
            'requiem': 18,
            'rich': 14,
            'ruo': 15,
            'tj':23,
            'vade': 16
        }
        num = users[member.lower()]
        return worksheet.cell(num, 2).value

    def get_fund_total(self):
        sheet = self.file.open_by_key(os.environ['Sheet_ID_2019'])
        worksheet = sheet.get_worksheet(0)
        val = worksheet.cell(25, 1).value
        return val


def setup(bot):
    bot.add_cog(NOHK(bot))
