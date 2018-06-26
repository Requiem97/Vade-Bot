import discord, random, datetime, json, gspread, os
from discord.ext import commands
from src.commands import VadeDeets
from src.db import connect

from oauth2client.service_account import ServiceAccountCredentials

class NOHK:
    "Views some cards saved before the death of Bully Bot"
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self):
        "Daily giveaway using the NOHK fund"
        date = datetime.datetime.now()
        amount = random.randint(20,30)
        if connect.hasData(VadeDeets.userID):
            if connect.canUse(VadeDeets.userID):
                connect.uploadData(VadeDeets.userID, amount, date)
                await self.bot.say("You got " + str(amount) + " Php from the fund.")
            else:
                wait = VadeDeets.wait.split(":")
                await self.bot.say("Please try again in " + wait[0] + " hours " + wait[1] + " minutes and " + wait[2] + " seconds.")
        else: 
            connect.createData(VadeDeets.userID, amount, date)
            await self.bot.say("You got " + str(amount) + " Php from the fund.")

    @commands.command()
    async def fund(self):
        "Get personal fund balance"
        connect.getFund(VadeDeets.userID)
        fund = connect.getFund(VadeDeets.userID)
        await self.bot.say ("You currently got " + str(fund) + " Php from the fund")
    
    @commands.group(pass_context=True)
    async def card (self, ctx):
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
        commonCards = [card.title() for card in VadeDeets.cardMap if "1" in card]
        uncommonCards = [card.title() for card in VadeDeets.cardMap if "2" in card]
        rareCards = [card.title() for card in VadeDeets.cardMap if "3" in card]
        specialCards = [card.title() for card in VadeDeets.cardMap if "4" in card]
        commonCards.sort()
        uncommonCards.sort()
        rareCards.sort()
        specialCards.sort()
        commonText = "__**Common Cards**__\n" + str(commonCards).strip("[]")
        uncommonText = "__**Uncommon Cards**__\n" + str(uncommonCards).strip("[]")
        rareText = "__**Rare Cards**__\n" + str(rareCards).strip("[]")
        specialText = "__**Special Cards**__\n" + str(specialCards).strip("[]")
        message = (commonText + "\n\n" + uncommonText + "\n\n" + rareText + "\n\n" + specialText).replace("'","")
        await self.bot.say(message)

    @commands.command()
    async def utang(self, member = None):
        "View the current debt of a member in the fund"
        if member == None:
            await self.bot.say("Specify a fund subscriber dumbass")
        else:
            scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
            service_account_info = json.loads(os.environ['Google_Key'])
            credentials = ServiceAccountCredentials._from_parsed_json_keyfile(service_account_info, scope)
            file = gspread.authorize(credentials)
            sheet = file.open_by_key('1HPtHR_HRqH-MmxXYUwwkecTInLYiRdvQLN-Wq4pLeRY')
            worksheet = sheet.get_worksheet(0)
            users = {
                'alkaeid': 14,
                'arvin': 15,
                'marx': 16,
                'otacom': 17,
                'requiem': 18,
                'rich': 19,
                'ruo': 20,
                'vade': 21
            }
            try:
                num = users[member.lower()]
                val = worksheet.cell(num, 2).value
                await self.bot.say(member + "'s current debt is " + str(val))
            except:
                await self.bot.say("SUMALI KA MUNA SA COLLECTION GAGO!")


def setup(bot):
    bot.add_cog(NOHK(bot))