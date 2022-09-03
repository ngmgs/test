import discord
import traceback
from discord.ext import commands
from discord.ext import tasks
from os import getenv
from datetime import datetime, timezone, timedelta, time


bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
channel_sent = None




"""
@bot.event
async def on_ready():
    global channel_sent 
    channel_sent = bot.get_channel(1012237139729199136)
    send_message_every_10sec.start() #定期実行するメソッドの後ろに.start()をつける    
"""

@tasks.loop(minutes=1)
async def send_message_every_10sec():         
    guild = bot.guilds[0]
    t_delta = timedelta(hours=9)
    JST = timezone(t_delta, 'JST')
    now = datetime.now(JST).strftime('%A/%H:%M')
    channel_sent = bot.get_channel(1012237139729199136)
    await channel_sent.send(now)    






send_message_every_10sec.start()
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
