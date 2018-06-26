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
                await self.bot.say("Please try again in " + VadeDeets.wait)
        else: 
            connect.createData(VadeDeets.userID, amount, date)
            await self.bot.say("You got " + str(amount) + " Php from the fund.")

    @commands.command()
    async def fund(self):
        "Get personal fund balance"
        connect.getFund(VadeDeets.userID)
        #fund = connect.getFund(VadeDeets.userID)
        await self.bot.say ("You currently got " + VadeDeets.fund + " Php from the fund")
    
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
        commonCards = [card for card in VadeDeets.cardMap if "1" in card]
        uncommonCards = [card for card in VadeDeets.cardMap if "2" in card]
        rareCards = [card for card in VadeDeets.cardMap if "3" in card]
        specialCards = [card for card in VadeDeets.cardMap if "4" in card]
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
    async def utang(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        service_account_info = service_account_info = """{"type": "service_account","project_id": "strange-wharf-208404","private_key_id": "001423203cc7547ef65b3b4a20f0159848332fb3","private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDbhbaobX/7GckH\\nsDP7Ly/Qbqzf5OPSEqzvBL2rYRryB6VlkjJ+oV9tIxWXl79Sjn/RXgctY9XtsQ8x\\nVxueezTqEbbdozB1kc6jSnfCj3RnFrUHWdtdBnaQnBBRy5vaFwZ45tTZViAragHT\\nEt3UK5i0AOxW/3FF9dg+sOsY2gX0FUi/63lBAGUFlZM1fpExsAMP/PmHSTVfkJTv\\nCRJJRgMIXkKsOJYP0X8p/4oTuiZkeYvjlfMTlG4/0zH0uc1GrE5CeYSN8IUjPYj2\\nlOEUveQjNvoimItNDQbGaU0MSsSQLIXhJ1krdc+rbuj+FYZbsrg38helYcw+1WQS\\na5F6esorAgMBAAECggEAAW241xbDVvR/gOvOIsvXUVFvEZPxQZw6gOG0hEmA/eM7\\n2dHeP0G4l8K7ML3dkmF4BnpIrKxyJ3ZYBXeuJ9VgbkeIO6AEwDcfM6PX7K23UbZt\\nnishCNVybxV867NaA8zTj3TdHL75PZ8WfPOp+uf/uegpoZVO/OgRLLNFDGfa0xBP\\nTrHjHVXb/4zIWjeyOpMZeljyRjLBnzo2Goyzp/I2D06RgMnH5fvhk8CmNwZDST6q\\nUrz4jjH/+mt7NJ57Kx8APF+i3H+OMYvBAImrne1HYwWzQ6p1LcpcGsieLOw85eXJ\\nRiCixoO6TAY/7Cxua4Cfe+dc0RytwHHMz38EyRRT6QKBgQD4AIcOiZArPzt8+3ZL\\n7ltgNhZcg9IEPrOZjXvkxbJhwfOV8VyIkmRz0ppJuCHYa52xP6WsapavcBxRd3+4\\nateJhi8K+lkeIw4kQzGl2JcjM7LFCaqh6cEQe0Ln4kO/p88nKIUVfuF8/URV+V6O\\nuKLilYMufZZxT9jg2LgYwd0rkwKBgQDimg+ZGeR4jcLi6BI05OWPrO2+PV6wsB6C\\nRvUx7Uwy0jHEOaOExxZGFYivTACPF8zOsZFDQlFfuO4F8Y9xO8RZEZndb1PCxpga\\n/za4oCcqZWkGXAW20bd3jtfJ+qkwpLpNqpUeEbeMwHIItd8gfh8mDMRPz5ADhoO2\\nXh4k7ff2CQKBgA7NuUIc5AYw2BQ1znHp4Hp1wA/1rmuicoYP8/1L78H2GdwxdByS\\n4HwpbhxIaXzJr7gM3I7WLfh68LXMNEuF1SfYYqZ9GyS5Yva3LBeCPkNTqrAoS48u\\nrN+W+/9rei/OjIcB3C/USxFy7MlVAVfznYV490OnK3vIEGIbjaGssM8RAoGALgVX\\n8aIekpVH5Ul4mSF7tehLCH3yQzQhnhfHKHKnLRMfZFjIauj8DxPEhMWMv4L352qM\\ns/o+CJDIVpCurzKSN/ypIR3BByfKMIFwnaJ5EdUytUXvKygAeNmb3bt4rRZnd+qT\\nCl5SxtU206oMPM8giFvDauoet3iUO291884Ys/ECgYBdr9UPXVCUDMz07Tdq3N99\\nJZZyweMUp/tP5PKPT8ApOwYfC/aODqazSsU+fh+ttsyYHbGyfpiD31LgrSGdxml/\\nV007PyJkW26k0xcI22UJ1ShFDXkhEMFmdJZx1wbSpySRkbB9i0QmpVx05lc1NScU\\n2x9RS+di8iMDHPKyc8IVbQ==\\n-----END PRIVATE KEY-----\\n","client_email": "vade-bot-fund@strange-wharf-208404.iam.gserviceaccount.com","client_id": "109778594931743065269","auth_uri": "https://accounts.google.com/o/oauth2/auth","token_uri": "https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vade-bot-fund%40strange-wharf-208404.iam.gserviceaccount.com"}"""
        service_account_info = json.loads(service_account_info)
        credentials = ServiceAccountCredentials._from_parsed_json_keyfile(service_account_info, scope)
        print(service_account_info["type"])

        file = gspread.authorize(credentials) # authenticate with Google
        sheet = file.open_by_key('1HPtHR_HRqH-MmxXYUwwkecTInLYiRdvQLN-Wq4pLeRY') # open sheet
        worksheet = sheet.get_worksheet(0)
        val = worksheet.cell(18, 2).value
        await self.bot.say("Your current debt is " + str(val))


def setup(bot):
    bot.add_cog(NOHK(bot))