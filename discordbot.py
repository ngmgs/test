import discord
import traceback
import re
from discord.ext import commands
from discord.ext import tasks
from os import getenv
from datetime import datetime, timezone, timedelta, time


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
is_text = {}
channel_sent = None


@bot.event
async def on_message(message: discord.Message):
    await _check_url(message)

async def _check_url(message: discord.Message):
    role = discord.utils.get(message.guild.roles, name="kagi")
    member = message.author
    pattern = pattern = re.compile(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")


    if message.author.bot:
        return
    # メッセージからURLを抽出
    url_list = re.findall(pattern, message.content)
    # もしメッセージにURLが含まれていたら
    if url_list:
        print("#" * 50)
        print("1時間以内に同じURLを送信したら削除する")
        # もし辞書にURLが登録されていたら(含まれていなかったらNoneが返る)
        if is_text.get(url_list[0], None) is not None:
            # 送信されていた時間を取り出す
            _sent_date = is_text[url_list[0]]
            print("辞書に登録されている発言時間は" + str(_sent_date))
            # もし差分が3600秒以上(1h)なら
            if (datetime.now() - _sent_date).seconds >= 3600:
                # 辞書のURLが持つ発言時間を更新して終了
                print("辞書のURL(" + url_list[0] + ")が持つ発言時間を更新")
                is_text[url_list[0]] = datetime.now()
            else:
                # 1h以内に投稿されていた場合削除
                print(url_list[0])
                print("そのURL(" + url_list[0] + ")が入ったメッセージが1時間以内に投稿されています。削除します。")
                alert_msg = await message.channel.send("そのURLが入ったメッセージが1時間以内に投稿されています。削除します。")
                await message.delete(delay=1)
                await alert_msg.delete(delay=3)
                return
        else:
            # 辞書にURLが登録されていなかったのでURLと発言時間を登録する
            print("辞書にURLと発言時間を登録")
            is_text[url_list[0]] = datetime.now()
            print(is_text)
    else:
        print("メッセージにURLはない")
        
    # 発言したメンバーに役職kagiを付与
    await member.add_roles(role, atomic=True)

    await bot.process_commands(message)


@tasks.loop(
    time=time(
        hour=4, minute=1,
        tzinfo=timezone(
            timedelta(hours=9)
        )
    )
)
async def send_message_every_10sec():
    guild = bot.guilds[0]
    t_delta = timedelta(hours=9)
    JST = timezone(t_delta, 'JST')
    now = datetime.now(JST).strftime('%A/%H:%M')
    await channel_sent.send(now)
    if now == 'Saturday/04:01':
        await channel_sent.send(now + "全員のkagi権限削除")
        role = discord.utils.get(guild.roles, name="kagi")
        norolemember = [i for i in guild.members]
        for i in norolemember:
            try:
                await i.remove_roles(role, atomic=True)
            except discord.Forbidden:
                print("権限が足りません")

        await channel_sent.send(now + "鍵部屋をプライベート解除")
        channel_sent2 = bot.get_channel(1012928069402636390)
        role2 = discord.utils.get(guild.roles, name="@everyone")
        await channel_sent2.set_permissions(role2, read_messages=True)

    if now == 'Tuesday/04:01':
        await channel_sent.send(now + "鍵部屋をプライベート化")
        channel_sent2 = bot.get_channel(1012928069402636390)
        role2 = discord.utils.get(guild.roles, name="@everyone")
        await channel_sent2.set_permissions(role2, read_messages=False)

@bot.event
async def on_ready():
    global channel_sent
    channel_sent = bot.get_channel(1012237139729199136)
    send_message_every_10sec.start()  # 定期実行するメソッドの後ろに.start()をつける

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
