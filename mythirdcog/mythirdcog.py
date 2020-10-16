from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class MyThirdCog(commands.Cog):
    """Description of the cog visible with [p]help MyThirdCog"""

    @commands.command()
    async def mythirdcom(self, ctx):
        """Description of myfirstcom visible with [p]help mythirdcom"""
        # Your code will go here
        await ctx.send("My third cog!")
