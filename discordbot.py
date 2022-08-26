from discord.ext import commands
from os import getenv
import traceback
import discord

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def neko(ctx):
    await ctx.send('にゃー')

    



token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
