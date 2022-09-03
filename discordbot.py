import discord
import traceback
from discord.ext import commands
from discord.ext import tasks
from os import getenv
from datetime import datetime, timezone, timedelta, time


bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
channel_sent = None




@tasks.loop(seconds=10)
async def loop():
    now = datetime.now(JST).strftime('%A/%H:%M')
    channel_sent = bot.get_channel(1012237139729199136)
    await channel_sent.send(now)    
    
loop.start()




token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
