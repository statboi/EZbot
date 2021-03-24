import discord
from discord.ext import commands
import json

class Hibye(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        f = open("dir.txt", "r")
        os.chdir(f.read())
        f.close()
        with open(r"bot\config.json") as f:
            data = json.load(f)
            for p in data["botSettings"]:
                if p["welcomeMessageOn"]=="true":
                    try:
                        channel = bot.get_channel(int(p["welcomeMessageChannelId"]))
                    except:
                        print(f"\033[1;31;40m[ERROR]\033[0;37;40m {member} joined {member.guild} but i wasn't able to get channel by ID, check is 'welcomeMessageChannelId' in config.json file correct, go here - https://github.com/statboi/EZbot#protips - and read about getting IDs.")
                    else:
                        await channel.send(p["welcomeMessage"].replace("[user]", member.mention).replace("[guild]", member.guild.name))
                if p["welcomeDmOn"]=="true":
                    try:
                        await member.send(p["welcomeDm"].replace("[user]", member.mention).replace("[guild]", member.guild.name))
                    except:
                        return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        f = open("dir.txt", "r")
        os.chdir(f.read())
        f.close()
        with open(r"bot\config.json") as f:
            data = json.load(f)
            for p in data["botSettings"]:
                if p["leaveMessageOn"]=="true":
                    try:
                        channel = bot.get_channel(int(p["leaveMessageChannelId"]))
                    except:
                        print(f"\033[1;31;40m[ERROR]\033[0;37;40m {member} leaved {member.guild} but i wasn't able to get channel by ID, check is 'leaveMessageChannelId' in config.json file correct, go here - https://github.com/statboi/EZbot#protips - and read about getting IDs.")
                    else:
                        await channel.send(p["leaveMessage"].replace("[user]", member.mention).replace("[guild]", member.guild.name))
                else:
                    return


def setup(bot):
    bot.add_cog(Hibye(bot))
