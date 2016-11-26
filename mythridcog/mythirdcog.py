from discord.ext import commands


# Classname should be CamelCase and the same spelling as the folder
class MyThirdCog:
    """Description of the cog visible with [p]help MyThirdCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mythirdcom(self):
        """Description of myfirstcom visible with [p]help mythirdcom"""
        # Your code will go here
        pass


def setup(bot):
    bot.add_cog(MyThirdCog(bot))
