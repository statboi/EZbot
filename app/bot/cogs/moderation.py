import discord
from discord.ext import commands
import json

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, reason=None):
        with open("features.json", "r") as fe:
            if json.load(fe)["kick"]=="1":
                with open("config.json") as f:
                    data = json.load(f)
                    for p in data["config"]:
                        bot_author = p["authorName"]
                        try:
                            await member.send(f"You got **kicked** from `{ctx.guild}` by `{ctx.author}` for `{reason}`")
                        except:
                            await member.kick(reason=reason)
                            embed=discord.Embed(title="Kick", color=0xffb83d)
                            embed.add_field(name="Successfully kicked member", value=member.mention, inline=False)
                            embed.add_field(name="Notification", value="I wasn't able to notify target about kick.", inline=False)
                            embed.add_field(name="Reason:", value=reason, inline=False)
                            embed.set_footer(text=f"Bot made by {bot_author}\nPowered by EZbot - https://github.com/statboi/EZbot")
                            await ctx.send(embed=embed)
                        else:
                            await member.kick(reason=reason)
                            embed=discord.Embed(title="Kick", color=0xffb83d)
                            embed.add_field(name="Successfully kicked member", value=member.mention, inline=False)
                            embed.add_field(name="Notification", value="Successfully notificated target about kick with DM.", inline=False)
                            embed.add_field(name="Reason:", value=reason, inline=False)
                            embed.set_footer(text=f"Bot made by {bot_author}\nPowered by EZbot - https://github.com/statboi/EZbot")
                            await ctx.send(embed=embed)
            else: return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, reason=None):
        with open("features.json", "r") as fe:
            if json.load(fe)["ban"]=="1":
                with open("config.json") as f:
                    data = json.load(f)
                    for p in data["config"]:
                        bot_author = p["authorName"]
                        try:
                            await member.send(f"You got **banned** from `{ctx.guild}` by `{ctx.author}` for `{reason}`")
                        except:
                            await member.ban(reason=reason)
                            embed=discord.Embed(title="Ban", color=0xffb83d)
                            embed.add_field(name="Successfully banned member", value=member.mention, inline=False)
                            embed.add_field(name="Notification", value="I wasn't able to notify target about ban.", inline=False)
                            embed.add_field(name="Reason:", value=reason, inline=False)
                            embed.set_footer(text=f"Bot made by {bot_author}\nPowered by EZbot - https://github.com/statboi/EZbot")
                            await ctx.send(embed=embed)
                        else:
                            await member.ban(reason=reason)
                            embed=discord.Embed(title="Ban", color=0xffb83d)
                            embed.add_field(name="Successfully banned member", value=member.mention, inline=False)
                            embed.add_field(name="Notification", value="Successfully notificated target about ban with DM.", inline=False)
                            embed.add_field(name="Reason:", value=reason, inline=False)
                            embed.set_footer(text=f"Bot made by {bot_author}\nPowered by EZbot - https://github.com/statboi/EZbot")
                            await ctx.send(embed=embed)
            else: return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount):
        with open("features.json", "r") as fe:
            if json.load(fe)["clear"]=="1":
                with open("config.json") as f:
                    data = json.load(f)
                    for p in data["config"]:
                        bot_author = p["authorName"]
                        await ctx.channel.purge(limit=amount)
                        embed=discord.Embed(color=0x2efcff)
                        embed.add_field(name="Clearing", value=f"Succesfuly deleted {amount} messages on {ctx.channel.mention} channel!", inline=False)
                        embed.set_footer(text=f"Bot made by {bot_author}\nPowered by EZbot - https://github.com/statboi/EZbot")
                        await ctx.send(embed=embed)
            else: return

def setup(bot):
    bot.add_cog(Moderation(bot))
