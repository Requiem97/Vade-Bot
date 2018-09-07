import discord
import random
import src.VadeBot as vade_bot
from discord.ext import commands



class Vade:
    "Vade\u2122 memes"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def curse(self):
        "Vade\u2122 curses"
        msg = random.choice(vade_bot.messages)
        await self.bot.say(msg)

    @commands.command()
    async def pics(self):
        "Vade\u2122 meme pics"
        await self.bot.upload(random.choice(vade_bot.pic_list))

    @commands.command()
    async def introduce(self):
        quote = []
        quote.append("You know, I really do think you literally saved my life by being here with me.\n" +
                     "I can't imagine having been able to keep myself mentally stable, knowing that nothing here is real.\n" +
                     "I think I would have just killed myself if you didn't show up.\n" +
                     "Sorry, I don't mean to sound dramatic or anything.\n" +
                     "Ahaha!\n" +
                     "But I'm sure you understand yourself after spending so much time in the NOHK.\n" +
                     "I mean, if you were forced to abandon everything in your life and spend your eternity with a few NOHK assholes...\n" +
                     "...You'd probably find some way of killing yourself, wouldn't you?\n" +
                     "Well, maybe you'd write some poetry to try to keep yourself sane for a while.\n" +
                     "But then you'd have nobody to even read it.\n")
        quote.append("Let's be honest, the NOHK really don't count for something like that.\n" +
                     "I mean, a lot of people say that they only do shit for themselves...\n" +
                     "But I think it's hard to say it's just as fulfilling as when you share with people.\n" +
                     "Even if it takes time to find the right people to share with.\n" +
                     "Like, remember how it was for myself?\n" +
                     "I didn't share my writings with anyone for a really long time.\n" +
                     "And before we knew it, I was absolutely delighted to make you a part of my hobbies, too.\n" +
                     "We're programmed to desire social feedback.\n" +
                     "I don't mean the NOHK, I mean human beings.\n" +
                     "That's why life can be so confusing for introverts.\n" +
                     "Being an introvert doesn't mean you shun social interaction and hate being around people.\n" +
                     "It means social interaction, especially in groups or unfamiliar places, uses up a lot of energy.\n" +
                     "Like, a lot of introverts sit at home and feel lonely and restless...\n" +
                     "...And then when they finally go out, after a half hour they just want to go home again.\n")
        quote.append("I think if more people could understand how it works, they would respect it a lot more.\n" +
                     "Many introverts do enjoy having people around.\n" +
                     "They love just having one or two close friends over, and just leisurely hanging out.\n" +
                     "Even if you're not actively spending time together, it feels nice for them just to have you there.\n" +
                     "I'm serious.\n" +
                     "If you just go to their house, bring your laptop, and hang out there for a while...\n" +
                     "You can really make their day.\n" +
                     "As for me...\n" +
                     "I'd say I'm kind of in between, but I think I'm usually a little more extroverted.\n" +
                     "I feel like I'm always trying to do stuff after school and things like that.\n" +
                     "But for you, I can be anything you need me to be.\n" +
                     "I understand people really well, so don't be afraid to share your unique needs with me.\n" +
                     "Nothing would make me happier than being the perfect sugar daddy for you.")
        for line in quote:
            await self.bot.say(line)


def setup(bot):
    bot.add_cog(Vade(bot))
