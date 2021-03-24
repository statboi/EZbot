import discord
from discord.ext import commands
import json
import os
from pypresence import Presence
os.system("cls")

with open("config.json", "r") as f:
    data = json.load(f)
    for p in data['config']:
        bot = commands.Bot(command_prefix = p["prefix"])
        bot.remove_command('help')

try:
    rpc_client_id = "824234721126776863"
    RPC = Presence(rpc_client_id)
    RPC.connect()
    RPC.update(state=f"Currently hosting bot using EZbot!", details="EZbot is python-based Discord bot creator, all you need to do is to host it. You can customize your bot in many aspects.", buttons=[{"label": "EZbot GitHub", "url": "https://github.com/statboi/EZbot"}])
except: print("Error connecting to Rich Presence.")

@bot.event
async def on_connect():
    print(f"\033[1;33;40m[Connected]\033[0;37;40m {bot.user.name} has succesfully connected to Discord servers, loading...")
    with open("config.json") as f:
        data = json.load(f)
        for p in data["botSettings"]:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(p["botStatus"].replace("[botName]", bot.user.name)))

@bot.event
async def on_ready():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    print("\033[1;32;40m[Ready]\033[0;37;40m Your bot is ready! Thank you for using EZbot, also check our Discord statistics bot - statboi: tiny.one/statboi!")

@bot.event
async def on_disconnect():
    print("\033[1;31;40m[Disconnected]\033[0;37;40m Error - Disconnected from Discord servers, please check your network or Discord servers status.")

@bot.event
async def on_message(message):
    with open("config.json", "r") as f:
        data = json.load(f)
        for p in data['config']:
            if message.content.startswith(f"{p['prefix']}help"):
                embed=discord.Embed(title="Help menu", description=f"{bot.user.name} by {p['authorName']} powered by [EZbot](https://github.com/statboi/EZbot)", color=0x24bdff)
                embed.add_field(name="Moderation commands", value="kick [member] {reason}\nban [member] {reason}\nclear [amount]\nslowmode [seconds]", inline=False)
                embed.add_field(name="Utility commands", value="COMING SOON", inline=False)
                await message.channel.send(embed=embed)

@bot.command()
async def switchcommand(ctx, command):
    with open(r"cogs\features.json") as f:
        data = json.load(f)
        if command in data:
            if data[command]=="1":
                await ctx.send(f"Turned off `{command}` command.")

with open("config.json", "r") as f:
    data = json.load(f)
    for p in data['config']:
        bot.run(p['token'])
