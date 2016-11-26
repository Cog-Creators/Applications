from discord.ext import commands


# Classname should be CamelCase and the same spelling as the folder
class MySecondCog:
    """Description of the cog visible with [p]help MySecondCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mysecondcom(self):
        """Description of myfirstcom visible with [p]help mysecondcom"""
        # Your code will go here
        pass


def setup(bot):
    bot.add_cog(MySecondCog(bot))
