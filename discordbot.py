import discord
import traceback
import asyncio
from discord.ext import commands
from discord.ext import tasks
from os import getenv
from datetime import datetime, timezone, timedelta, time


bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
channel_sent = None




@tasks.loop(seconds=10)
async def loop():
    print("aaa")  
    
loop.start()




token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
