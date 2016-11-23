# Import random from the standard library so we can pick random numbers.
import random
from discord.ext import commands


class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def guess(self, ctx):
        """Guess what number I am thinking!"""
        # Grab the author object
        author = ctx.message.author
        # Make the bot output a prompt for the user
        await self.bot.say("Guess a number from 1 to 10.")
        # We use wait_for_message() to capture the response
        # You can set a timeout for how long they have to respond. Will make guess None.
        # Author is the object it should be expecting the response from.
        # Check let's you pass a regular function to perform advanced checks.
        guess = await self.bot.wait_for_message(timeout=15, author=author, check=self.digit_check)
        # Pick a number 1 through 10
        answer = random.randint(1, 10)
        # Now we run the logic to determine the right output.
        # When checking for no response, we simply use guess is None
        # When checking the author's input, we need to use guess.content
        # If the response.content does not equal our answer then it is wrong and moves to else
        if guess is None:
            msg = "Sorry, you took too long. I was thinking {}."
        elif int(guess.content) == answer:
            msg = "You are right! I was thinking {} too!"
        else:
            msg = "Sorry. I was actually thinking {}."
        await self.bot.say(msg.format(answer))

    # We write a function for our check(optional)
    # Because the response is a string. We need to determine, for example, if "10" is 10
    # If this throws an error(exception), then the exception is propagated.
    # The guess will not be accepted, unless this function runs without an exception.
    def digit_check(self, message):
            return message.content.isdigit()


def setup(bot):
    bot.add_cog(Mycog(bot))
