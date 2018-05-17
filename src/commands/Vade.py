import discord
from discord.ext import commands
import random
from src.commands import VadeDeets


class Vade:
    "Vade\u2122 memes"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def curse(self):
        "Vade\u2122 curses"
        msg = random.choice(VadeDeets.messages)
        await self.bot.say(msg)

    @commands.command()
    async def pics(self):
        "Vade\u2122 meme pics"
        await self.bot.upload(random.choice(VadeDeets.picList))

    @commands.command()
    async def introduce(self):
        quote = """You know, I really do think you literally saved my life by being here with me.
I can't imagine having been able to keep myself mentally stable, knowing that nothing here is real.
I think I would have just killed myself if you didn't show up.
Sorry, I don't mean to sound dramatic or anything.
Ahaha!
But I'm sure you understand yourself after spending so much time in the NOHK.
I mean, if you were forced to abandon everything in your life and spend your eternity with a few NOHK assholes...
...You'd probably find some way of killing yourself, wouldn't you?
Well, maybe you'd write some poetry to try to keep yourself sane for a while.
But then you'd have nobody to even read it.
Let's be honest, the NOHK really don't count for something like that.
I mean, a lot of people say that they only do shit for themselves...
But I think it's hard to say it's just as fulfilling as when you share with people.
Even if it takes time to find the right people to share with.
Like, remember how it was for myself?
I didn't share my writings with anyone for a really long time.
And before we knew it, I was absolutely delighted to make you a part of my hobbies, too.
We're programmed to desire social feedback.
I don't mean the NOHK, I mean human beings.
That's why life can be so confusing for introverts.
Being an introvert doesn't mean you shun social interaction and hate being around people.
It means social interaction, especially in groups or unfamiliar places, uses up a lot of energy.
Like, a lot of introverts sit at home and feel lonely and restless...
...And then when they finally go out, after a half hour they just want to go home again.
I think if more people could understand how it works, they would respect it a lot more.
Many introverts do enjoy having people around.
They love just having one or two close friends over, and just leisurely hanging out.
Even if you're not actively spending time together, it feels nice for them just to have you there.
I'm serious.
If you just go to their house, bring your laptop, and hang out there for a while...
You can really make their day.
As for me...
I'd say I'm kind of in between, but I think I'm usually a little more extroverted.
I feel like I'm always trying to do stuff after school and things like that.
But for you, I can be anything you need me to be.
I understand people really well, so don't be afraid to share your unique needs with me.
Nothing would make me happier than being the perfect sugar daddy for you."""
        await self.bot.say(quote)
        


def setup(bot):
    bot.add_cog(Vade(bot))
