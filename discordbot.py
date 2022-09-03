import discord
from discord.ext import commands
from discord.ext import tasks


bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
channel_sent = None




@tasks.loop(seconds=10)
async def loop_10sec():
    print("aaa")  
    
loop_10sec.start()





token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
