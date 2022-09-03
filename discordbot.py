import discord
import traceback
import asyncio
from discord.ext import commands
from discord.ext import tasks
from os import getenv

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())



@tasks.loop(seconds=10)
async def loop_10sec():
    print("aaa")  

async def fn():
    await loop_10sec.start()

loop_ = asyncio.get_event_loop()
loop_.run_until_complete(fn())

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
