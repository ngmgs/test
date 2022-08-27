import discord
import traceback
from discord.ext import commands
from os import getenv


bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
           

@bot.event
async def on_ready():
    guild = bot.guilds[0]
    norolemember = [i for i in guild.members]
    norolemember2 = [i for i in guild.members if len(i.roles) == 1]
    print("on_ready")
    print(discord.__version__)
    print(norolemember)
    for item in norolemember:
        print(item)       
   
    print("on_ready")
    print(discord.__version__)
    print(norolemember2)
    for item in norolemember2:
        print(item)     
        
        
@bot.command()
async def test(ctx):
    guild = bot.guilds[0]
    norolemember = [i for i in guild.members]
    norolemember2 = [i for i in guild.members if len(i.roles) == 1]

    for item in norolemember:
        await ctx.send(item)
    
    await ctx.send(discord.__version__)
    
    for item in norolemember2:
        await ctx.send(item)          
        await item.kick()         
        
@bot.command()
async def tes(ctx):
    guild = bot.guilds[0]
    norolemember = [i for i in guild.members]
    norolemember2 = [i for i in guild.members if len(i.roles) == 2]

    for item in norolemember:
        await ctx.send(item)
    
    await ctx.send(discord.__version__)
    
    for item in norolemember2:
        await ctx.send(item)    
      
       
@bot.command()    
async def norole(ctx, message): #guildオブジェクトを渡してください
    guild = bot.guilds[0]
    role = discord.utils.get(message.guild.roles, name = "kagi")
    norolemember = [i for i in guild.members]
    for i in norolemember:
        try:
            await ctx.send(i)
            await i.remove_roles(role, atomic=True)    
        except discord.Forbidden:
            print("権限が足りません")













@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    

@bot.command()
async def ping(ctx):
    await ctx.send(discord.__version__)
    
    
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member, reason):
   await member.kick(reason=reason)
   embed=discord.Embed(title="KICK", color=0xff0000)
   embed.add_field(name="メンバー", value=f"{member.mention}", inline=False)
   embed.add_field(name="理由", value=f"{reason}", inline=False)
   await ctx.send(embed=embed)


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
