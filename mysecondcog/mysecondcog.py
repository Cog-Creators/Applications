from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class MySecondCog:
    """Description of the cog visible with [p]help MySecondCog"""

    @commands.command()
    async def mysecondcom(self, ctx):
        """Description of myfirstcom visible with [p]help mysecondcom"""
        # Your code will go here
        await ctx.send("My second cog!")
