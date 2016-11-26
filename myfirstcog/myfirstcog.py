from discord.ext import commands


# Classname should be CamelCase and the same spelling as the folder
class MyFirstCog:
    """Description of the cog visible with [p]help MyFirstCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def myfirstcom(self):
        """Description of myfirstcom visible with [p]help myfirstcom"""
        # Your code will go here
        pass


def setup(bot):
    bot.add_cog(MyFirstCog(bot))
