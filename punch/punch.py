import discord
from discord.ext import commands


class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    # Allow the command pass the context. Context is all the captured information when
    # Someone invokes a command. Make ctx your second argument to store the information.
    @commands.command(pass_context=True)
    async def punch(self, ctx, user: discord.Member):
        """I will punch anyone! >.<"""
        # Get the object of the person who invoked the command.
        # You can explore author using .mention, .id, .name, and many others.
        author = ctx.message.author
        # You can preformat a message before outputting to the bot.
        msg = "ONE PUNCH! {} knocked {} out cold! ლ(ಠ益ಠლ)".format(author.mention, user.mention)

        # Your code will go here.
        await self.bot.say(msg)


def setup(bot):
    bot.add_cog(Mycog(bot))
